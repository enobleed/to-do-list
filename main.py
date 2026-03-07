from enum import Enum
from dataclasses import dataclass, field
import json
from datetime import datetime

save_file = 'tasks.json'

class Status(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'

@dataclass
class Task:
    task_id: int
    description: str
    status: Status =  Status.TODO
    created_at: str = datetime.now().isoformat()
    updated_at: str = created_at

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

def save_tasks(tasks):
    with open(save_file, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def load_tasks():
    try:
        with open(save_file, 'r') as f:
            return [
                Task(
                t['task_id'],
                t['description'],
                Status(t['status']),
                t['created_at'],
                t['updated_at'])
                for t in json.load(f)]
    except FileNotFoundError:
        return []

def print_tasks(tasks, category=False):
    for task in tasks:
        if not category or task.status == category:
            print(task)

def parse_description(command):
    started = 0
    ended = len(command) - 1
    if command[ended] != '"':
        return False
    for i in range(ended):
        if command[i] == '"':
            started = i
            break
    else:
        return False
    return command[started + 1:ended]

def get_id(tasks):
    ids = {t.task_id for t in tasks}
    for i in range(1, len(ids)+2):
        if i not in ids:
            return i
    return 0

def cli(tasks):
    while True:
        command = input('Enter command > ')
        match command.split():
            case ['quit'] | ['q']:
                break
# list
            case ['list']:
                print('List of all tasks')
                print_tasks(tasks)
            case 'list', 'done' | 'todo' | 'in-progress' as status:
                print_tasks(tasks, status)
            case 'list', *wtv:
                print('Incorrect status')
# add
            case ['add']:
                print('Please enter a task')
            case 'add', *info:
                description = parse_description(command)
                if description:
                    tasks.append(Task(get_id(tasks), description))
                    print (f'Added task: {description}')
                else:
                    print('Please enter a task within double quotes')
# update
            case 'update', task_id:
                if task_id.isdigit():
                    print(f'Please enter an update')
                else:
                    print('Invalid id')
            case 'update', task_id, *info:
                if not task_id.isdigit():
                    print('Invalid id')
                    continue
                description = parse_description(command)
                if description:
                    print (f'Updating task: {description} for id: {task_id}')
                else:
                    print('Please enter a task within double quotes')
            case ['update']:
                print('Please enter task id and then task within double quotes')
            case 'update', *wtv:
                print('Invalid id')
# delete
            case 'delete', task_id:
                if task_id.isdigit():
                    print(f'Deleting task with id: {task_id}')
                else:
                    print('Invalid id')
            case ['delete']:
                print('Please enter task id')
            case 'delete', *wtv:
                print('Invalid id')
# mark
            case 'mark-in-progress' | 'mark-done' as status, task_id:
                if task_id.isdigit():
                    status = status.replace('mark-', '')
                    print(f'Changing status to {status} for id: {task_id}')
                else:
                    print('Invalid id')

if __name__ == '__main__':
    list_tasks = load_tasks()
    cli(list_tasks)
    save_tasks(list_tasks)