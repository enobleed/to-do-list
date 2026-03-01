
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
                print (f'Adding task: {info}')






if __name__ == '__main__':
    main()