from utils import tasks_list_file, does_task_exist, format_time

def add_time_to_task(task_name):
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    time_added = int(input("Enter the time to add (in minutes): "))

    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    for line_index, line in enumerate(lines):
        if task_name in line:
            importance = int(line.split(",")[1])

            current_time = int(line.split(",")[2])
            new_time = current_time + time_added

            updated_line = f"{task_name},{importance},{new_time}\n"
            lines[line_index] = updated_line
            break

    with open(tasks_list_file, "w") as file:
        file.writelines(lines)

    print(f"Time added to '{task_name}' successfully.")

def display_task_times():
    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No tasks exist. Create a new task to get started.")
        return

    print("Tasks:")

    for line in lines:
        task_name, importance, time_invested = line.strip().split(",")

        formatted_time = format_time(int(time_invested))
        print(f"\t- {task_name}: {formatted_time}")

def TimeTracker():
    display_task_times()

    option = input("\nTIME TRACKER - Choose an option\n1. Add time to a task\n2. Display time invested\nEnter your choice: ")

    if option == "1":
        task_name = input("Enter the task name: ")
        add_time_to_task(task_name)

    elif option == "2":
        display_task_times()

    else:
        print("Invalid option.")
