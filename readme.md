# Simple Task Tracker

This is a simple task tracker script that allows you to create, delete, and add time to tasks. It stores task data in a text file named `task_data.txt`.

## Usage

To run the script, simply save it as a `.py` file and execute it using the Python interpreter. The script will prompt you with a menu to select an option:

1. Create a new task
2. Delete an existing task
3. Add time to a task
4. Display tasks
5. Exit

### Example Usage

```bash
python task_tracker.py
```

### Functions

The script includes the following functions:

* `does_task_exist(task_name)`: Checks if the specified task already exists
* `create_task(task_name)`: Creates a new task with the given name
* `delete_task(task_name)`: Deletes the specified task
* `add_time(task_name)`: Adds the specified amount of time to the given task
* `format_time(time_in_minutes)`: Formats the time in minutes to hours and minutes
* `display_tasks()`: Displays a list of all tasks and the time invested in each task

### Installation

No installation is required. Simply save the script as a `.py` file and run it using the Python interpreter.
