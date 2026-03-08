# Todo CLI

A simple command line task manager written in Python.
The application allows you to create, update, delete and manage tasks directly from the terminal. Tasks are stored in a JSON file so they persist between sessions.

# Basic Features:

- Add new tasks
- Update task description
- Change task status
- Delete tasks
- List tasks
- Filter tasks by status
- Persistent storage using JSON
- Automatic timestamps for creation and updates

# Usage

Add a task
add "<task_description>"
```
add "Buy milk"
```
List tasks
list <task_status>
```
list
list done
list todo
list in-progress
```
Update task
update <task_id> "<new_task_description>"
```
update 2 "Buy bread instead"
```
Delete task
delete <task_id>
```
delete 2
```
Change task status
```
mark-done 2
mark-in-progress 2
```
Exit
```
quit
q
```

https://roadmap.sh/projects/task-tracker
