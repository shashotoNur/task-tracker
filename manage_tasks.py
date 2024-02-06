"""Module containing the menu for managing tasks"""

from utils import TASKS_LIST_FILE, does_task_exist
from utils import format_time, print_table

def create_task(task_name, importance):
    """Function for creating new tasks"""
    task_exists = does_task_exist(task_name)

    if task_exists:
        print(f"Task '{task_name}' already exists.")
        return

    target = input("Add a time target to the task in minutes ('0' to skip): ")

    with open(TASKS_LIST_FILE, "a", encoding="utf-8") as file:
        file.write(f"{task_name},{importance},0,{target}\n")

    print(f"Task '{task_name}' created successfully.")

def delete_task(task_name):
    """Function for removing existing tasks"""
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        if task_name not in line:
            new_lines.append(line)

    with open(TASKS_LIST_FILE, "w", encoding="utf-8") as file:
        file.writelines(new_lines)

    print(f"Task '{task_name}' deleted successfully.")

def edit_task(task_name, criteria):
    """Function for modifying performance or target of a task"""
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []
    index = 1 if "Importance" in criteria[0] else 3

    for line in lines:
        if task_name in line:
            data = line.split(",")

            data[index] = criteria[1]
            data[3] = data[3].rstrip('\n') + '\n'

            line = ','.join(data)

        new_lines.append(line)

    with open(TASKS_LIST_FILE, "w", encoding="utf-8") as file:
        file.writelines(new_lines)

    print(f"Task '{task_name}' successfully updated with {criteria[0]} at {criteria[1]}.")

def list_all_tasks():
    """Function to list all of the existing tasks"""
    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    table_data = [
        ['Task', 'Importance', 'Time Invested', 'Target']
    ]

    for line in lines:
        table_row = line.split(",")
        table_row[2] = format_time(int(table_row[2]))

        if table_row[3] == '0\n' or table_row[3] == '0':
            table_row[3] = 'None'
        else:
            table_row[3] = format_time(int(table_row[3]))

        table_data.append(table_row)

    print_table(table_data)

def task_manager():
    """Menu for managing tasks"""
    list_all_tasks()

    print("TASK MANAGER - Choose an option")
    print("1. Create a new task")
    print("2. Delete an existing task")
    print("3. Edit task importance or time target")
    option = input("4. Go back\nEnter your choice: ")

    if option == "1":
        task_name = input("Enter the task name: ")
        importance = int(input("Enter the importance of the task in integer: "))

        create_task(task_name, importance)

    elif option == "2":
        task_name = input("Enter the task name to delete: ")
        delete_task(task_name)

    elif option == "3":
        task_name = input("Enter the task name to update: ")
        print("Enter the criteria to update: ")
        choice = input("1. Importance\n2. Time Target\nEnter your choice: ")

        key = "Importance (number > 0)" if choice == "1" else "Target (in minutes)"
        value = input(f"Enter the value for {key}: ")

        edit_task(task_name, [key, value])

    else:
        return
