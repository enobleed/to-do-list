from enum import Enum
import json
from datetime import datetime

save_file = 'tasks.json'

class Status(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'

class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.status = Status.TODO
        self.created_at = self.get_time()
        self.updated_at = self.created_at

    def task_from_dict(data):
        task = Task(data['task_id'], data['description'])
        task.status = Status(data['status'])
        task.created_at = data['created_at']
        task.updated_at = data['updated_at']
        return task

    def get_time(self):
        return datetime.now().strftime('%d.%m.%Y %H:%M:%S')

    def update_description(self, description):
        self.description = description
        self.updated_at = self.get_time()

    def update_status(self, status):
        if status in Status:
            self.status = Status(status)
            self.updated_at = self.get_time()
            return True
        return False

    def to_dict(self):
        return {
            'task_id': self.task_id,
            'description': self.description,
            'status': self.status.value,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def __str__(self):
        return f'[{self.task_id}] {self.description} ({self.status.value})'

def save_tasks(tasks):
    with open(save_file, 'w') as f:
        json.dump([t.to_dict() for t in tasks], f, indent=4)

def load_tasks():
    try:
        with open(save_file, 'r') as f:
            return [Task.task_from_dict(t) for t in json.load(f)]
    except FileNotFoundError, json.decoder.JSONDecodeError:
        return []

def print_tasks(tasks, category=False):
    for task in tasks:
        if not category or task.status.value == category:
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
                task_id = int(task_id)
                description = parse_description(command)
                if description:
                    for t in tasks:
                        if t.task_id == task_id:
                            t.update_description(description)
                            print(f'Updated task: {description} for id: {task_id}')
                            break
                    else:
                        print('No such id')
                else:
                    print('Please enter a task within double quotes')
            case ['update']:
                print('Please enter task id and then task within double quotes')
            case 'update', *wtv:
                print('Invalid id')
# delete
            case 'delete', task_id:
                if task_id.isdigit():
                    task_id = int(task_id)
                    for i in range(len(tasks)):
                        if tasks[i].task_id == task_id:
                            print(f'Deleting task {tasks[i].description} with id: {task_id}')
                            del tasks[i]
                            break
                    else:
                        print('No such id')
                else:
                    print('Invalid id')
            case ['delete']:
                print('Please enter task id')
            case 'delete', *wtv:
                print('Invalid id')
# mark
            case 'mark-in-progress' | 'mark-done' as status, task_id:
                if task_id.isdigit():
                    task_id = int(task_id)
                    status = status.replace('mark-', '')
                    for t in tasks:
                        if t.task_id == task_id:
                            if t.update_status(status):
                                print(f'Changed status to {status} for task with id: {task_id}')
                            else:
                                print('Wrong status')
                            break
                    else:
                        print('No such id')
                else:
                    print('Invalid id')

if __name__ == '__main__':
    list_tasks = load_tasks()
    cli(list_tasks)
    save_tasks(list_tasks)