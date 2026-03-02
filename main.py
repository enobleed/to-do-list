
class Task:
    def __init__(self, task_id, description, status, created_at, updated_at):
        self.task_id = task_id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

def print_tasks(category='all'):
    pass

def main():
    while True:
        command = input('Enter command > ')
        match command.split():
            case ['quit'] | ['q']:
                exit(0)
            case ['list']:
                print('List of all tasks')
                print_tasks()
            case 'list', 'done':
                print('List of all tasks done')
                print_tasks('done')
            case 'list', 'todo':
                print('List of all tasks todo')
                print_tasks('todo')
            case 'list', 'in-progress':
                print('List of all tasks in-progress')
                print_tasks('in-progress')
            case 'list', *wtv:
                print('Incorrect category')
            case ['add']:
                print('Please enter a task')
            case 'add', *info:
                task = ' '.join(info)
                if task[0] == task[-1] == '"':
                    task = task[1:-1]
                    print (f'Adding task: {task}')
                else:
                    print('Please enter a task with "+"')
            case 'update', task_id:
                if task_id.isdigit():
                    print(f'Updating task with id: {task_id}')
                else:
                    print('Invalid id')
            case ['update']:
                print('Please enter task id')
            case 'update', *wtv:
                print('Invalid id')

if __name__ == '__main__':
    main()