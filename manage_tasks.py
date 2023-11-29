from utils import tasks_list_file, does_task_exist, format_time, print_table

def create_task(task_name, importance):
    task_exists = does_task_exist(task_name)

    if task_exists:
        print(f"Task '{task_name}' already exists.")
        return

    with open(tasks_list_file, "a") as file:
        file.write(f"{task_name},{importance},0\n")

    print(f"Task '{task_name}' created successfully.")

def delete_task(task_name):
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        if task_name not in line:
            new_lines.append(line)

    with open(tasks_list_file, "w") as file:
        file.writelines(new_lines)

    print(f"Task '{task_name}' deleted successfully.")

def edit_task_importance(task_name, importance):
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        if task_name in line:
            time_invested = line.split(",")[2]
            line = f"{task_name},{importance},{time_invested}"
        new_lines.append(line)

    with open(tasks_list_file, "w") as file:
        file.writelines(new_lines)

    print(f"Task '{task_name}' successfully updated with importance at {importance}.")

def list_all_tasks():
    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    table_data = [
        ['Task', 'Importance', 'Time Invested']
    ]

    for line in lines:
        table_row = line.split(",")
        table_row[2] = format_time(int(table_row[2]))
        table_data.append(table_row)

    print_table(table_data)

def TaskManager():
	option = input("\nTASK MANAGER - Choose an option\n1. Create a new task\n2. Delete an existing task\n3. Update the importance of a task\n4. List all tasks\nEnter your choice: ")

	if option == "1":
		task_name = input("Enter the task name: ")
		importance = int(input("Enter the importance of the task in integer: "))
		create_task(task_name, importance)

	elif option == "2":
		task_name = input("Enter the task name to delete: ")
		delete_task(task_name)

	elif option == "3":
		task_name = input("Enter the task name to update: ")
		importance = int(input("Enter the importance of the task (0-100): "))
		edit_task_importance(task_name, importance)

	elif option == "4":
		list_all_tasks()

	else:
		print("Invalid option.")
