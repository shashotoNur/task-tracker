import os

data_file = "task_data.txt"

def does_task_exist(task_name):
    with open(data_file, "r") as file:
        lines = file.readlines()
    file.close()

    for line in lines:
        if task_name in line:
            return True

    return False

def create_task(task_name):
    task_exists = does_task_exist(task_name)

    if task_exists:
        print(f"Task '{task_name}' already exists.")
        return

    with open(data_file, "a") as file:
        file.write(f"{task_name},0\n")
    file.close()

    print(f"Task '{task_name}' created successfully.")

def delete_task(task_name):
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(data_file, "r") as file:
        lines = file.readlines()
    file.close()

    new_lines = []

    for line in lines:
        if task_name not in line:
            new_lines.append(line)

    with open(data_file, "w") as file:
        file.writelines(new_lines)
    file.close()

    print(f"Task '{task_name}' deleted successfully.")

def add_time(task_name):
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    time_added = int(input("Enter the time to add (in minutes): "))

    with open(data_file, "r") as file:
        lines = file.readlines()
    file.close()

    for line_index, line in enumerate(lines):
        if task_name in line:
            current_time = int(line.split(",")[-1])
            new_time = current_time + time_added

            lines[line_index] = f"{task_name},{new_time}\n"
            break

    with open(data_file, "w") as file:
        file.writelines(lines)
    file.close()

    print(f"Time added to '{task_name}' successfully.")

def format_time(time_in_minutes):
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60

    formatted_time = ""

    if hours > 0:
        formatted_time += f"{hours} hours, "

    formatted_time += f"{minutes} minutes"
    return formatted_time

def display_tasks():
    with open(data_file, "r") as file:
        lines = file.readlines()
    file.close()

    if len(lines) == 0:
        print("No tasks exist. Create a new task to get started.")
        return

    print("Tasks:")

    for line in lines:
        task_name, time_invested = line.strip().split(",")
        formatted_time = format_time(int(time_invested))

        print(f"\t- {task_name}: {formatted_time}")

def main():
    if not os.path.exists(data_file):
        with open(data_file, "a") as file:
            file.write("")
        file.close()

    display_tasks()

    while True:
        input("Press enter to continue...")

        option = input("\nMENU - Choose an option\n1. Create a new task\n2. Delete an existing task\n3. Add time to a task\n4. Display tasks\n5. Exit\nEnter your choice: ")

        if option == "1":
            task_name = input("Enter the task name: ")
            create_task(task_name)
        elif option == "2":
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif option == "3":
            task_name = input("Enter the task name: ")
            add_time(task_name)
        elif option == "4":
            display_tasks()
        elif option == "5":
            print("Exiting the task tracker.")
            break
        else:
            print("Invalid option. Please choose between 1 to 5.")

if __name__ == "__main__":
    main()
