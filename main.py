from enum import Enum
from dataclasses import dataclass
from datetime import datetime

class Status(Enum):
    TODO = 'todo'
    IN_PROGRESS = 'in-progress'
    DONE = 'done'

@dataclass
class Task:
    task_id: int
    description: str
    status: Status.TODO
    created_at: str
    updated_at: str

def print_tasks(category='all'):
    pass

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

def main():
    while True:
        command = input('Enter command > ')
        match command.split():
            case ['quit'] | ['q']:
                exit(0)
            case ['list']:
                print('List of all tasks')
                print_tasks()
            case 'list', 'done' | 'todo' | 'in-progress' as status:
                print_tasks(status)
            case 'list', *wtv:
                print('Incorrect status')
            case ['add']:
                print('Please enter a task')
            case 'add', *info:
                task = parse_description(command)
                if task:
                    print (f'Adding task: {task}')
                else:
                    print('Please enter a task within double quotes')
            case 'update', task_id:
                if task_id.isdigit():
                    print(f'Please enter an update')
                else:
                    print('Invalid id')
            case 'update', task_id, *info:
                if not task_id.isdigit():
                    print('Invalid id')
                    continue
                task = parse_description(command)
                if task:
                    print (f'Updating task: {task} for id: {task_id}')
                else:
                    print('Please enter a task within double quotes')
            case ['update']:
                print('Please enter task id and then task within double quotes')
            case 'update', *wtv:
                print('Invalid id')
            case 'delete', task_id:
                if task_id.isdigit():
                    print(f'Deleting task with id: {task_id}')
                else:
                    print('Invalid id')
            case ['delete']:
                print('Please enter task id')
            case 'delete', *wtv:
                print('Invalid id')
            case 'mark-in-progress' | 'mark-done' as status, task_id:
                if task_id.isdigit():
                    status = status.replace('mark-', '')
                    print(f'Changing status to {status} for id: {task_id}')
                else:
                    print('Invalid id')

if __name__ == '__main__':
    main()