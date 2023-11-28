import os
import datetime

# Define the file names for storing task data
current_month_file = f"task_performances_{datetime.datetime.now().strftime('%Y_%m')}.txt"
task_list_file = "task_list.txt"

# Function to check if a task exists in the all_tasks file
def does_task_exist(task_name):
    if not os.path.exists(task_list_file):
        return False

    with open(task_list_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        task_data = line.strip().split(",")
        if task_name == task_data[0]:
            return True

    return False

def get_task_relative_importance(task_name):
    importance = 0
    total_importance = 0

    with open(task_list_file, "r") as file:
        for line in file:
            task_data = line.strip().split(",")
            total_importance += int(task_data[1])
            if task_name in line:
                importance = int(task_data[1])

    return importance / total_importance

# Function to create a new task in the all_tasks file
def create_task(task_name, importance):
    with open(task_list_file, "a") as file:
        file.write(f"{task_name},{importance}\n")

    print(f"Task '{task_name}' created successfully.")

# Function to delete a task from the all_tasks file
def delete_task(task_name):
    if not os.path.exists(task_list_file):
        return

    with open(task_list_file, "r") as file:
        lines = file.readlines()

    new_lines = []
    for line in lines:
        task_data = line.strip().split(",")
        if task_name != task_data[0]:
            print(line)
            new_lines.append(line)

    with open(task_list_file, "w") as file:
        file.writelines(new_lines)

    print(f"Task '{task_name}' deleted successfully.")

# Function to check if the current month file exists, create it if not
def ensure_current_month_file_exists():
    if not os.path.exists(current_month_file):
        with open(current_month_file, "w") as file:
            file.write("")

# Function to set the performance of a task for the current day
def set_task_performance(task_name, performance):
    ensure_current_month_file_exists()

    current_date = datetime.datetime.now().strftime("%d-%m-%Y")

    with open(current_month_file, "r") as file:
        lines = file.readlines()

    new_lines = []

    task_is_to_be_written = False
    date_found = False
    line_to_be_added = f"{task_name},{performance}"

    for lineNumber, line in enumerate(lines):
        new_lines.append(line)
        task_in_line = line.strip().split(",")[0]

        if current_date in line:
            task_is_to_be_written = True
            date_found = True
        elif task_is_to_be_written and task_name == task_in_line:
            print(f"Performance for today's '{task_name}' is already set.")
            task_is_to_be_written = False
        elif task_is_to_be_written and lineNumber == (len(lines)-1):
            new_lines.append(f"\n{line_to_be_added}")
            task_is_to_be_written = False
            print(f"Performance for task '{task_name}' set successfully.")

    if not date_found:
        new_lines.append(f"\n{current_date}\n{line_to_be_added}")
        print(f"Performance for task '{task_name}' set successfully.")

    with open(current_month_file, "w") as file:
        file.writelines(new_lines)

# Function to display a list of all tasks with their performance on that day
def display_tasks(date):
    ensure_current_month_file_exists()

    date_object = datetime.datetime.strptime(date, "%d-%m-%Y")
    next_date_object = date_object + datetime.timedelta(days=1)

    next_date = next_date_object.strftime("%d-%m-%Y")
    found_date = False
    tasks_exist = False

    with open(current_month_file, "r") as file:
        lines = file.readlines()

    print(f"Task performances for {date}:")
    for line in lines:
        if date in line:
            found_date = True
        elif found_date:
            task_data = line.strip().split(",")
            if task_data[0] == '':
                break
            print(f"\t- {task_data[0]}: {task_data[1]}")
            tasks_exist = True
        elif next_date in line:
            break

    if not tasks_exist:
        print(f"No tasks on {date}.")

def get_performance_of_day(date):
    found_date = False
    collective_performance = 0

    with open(current_month_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if date in line:
            found_date = True
        elif found_date:
            task_data = line.strip().split(",")
            if task_data[0] == '':
                break
            relative_importance = get_task_relative_importance(task_data[0])
            collective_performance += relative_importance * int(task_data[1])

    return collective_performance

def get_performance_of_a_range_of_days(start_date, end_date):
    start_date_obj = datetime.datetime.strptime(start_date, '%d-%m-%Y')
    end_date_obj = datetime.datetime.strptime(end_date, '%d-%m-%Y')

    num_days = (end_date_obj - start_date_obj).days + 1
    total_performance = 0

    while start_date_obj <= end_date_obj:
        total_performance += get_performance_of_day(start_date_obj.strftime("%d-%m-%Y"))
        start_date_obj += datetime.timedelta(days=1)

    return total_performance / num_days

# Define the main function
def main():
    # Check if the data file exists, create it if not
    if not os.path.exists(task_list_file):
        with open(task_list_file, "a") as file:
            file.write("")

    # Display a list of all tasks with their performance on that day
    display_tasks(datetime.datetime.now().strftime("%d-%m-%Y"))

    while True:
        input("Press enter to continue...")
        # Show a menu and get user input
        option = input("\nChoose an option:\n1. Create a new task\n2. Delete an existing task\n3. Set performance for a task\n4. Display tasks\n5. Get performance of a day\n6. Display overall performance within a date range\n7. Exit\nEnter your choice: ")

        if option == "1":
            task_name = input("Enter the task name: ")
            importance = int(input("Enter the importance of the task (0-100): "))

            if does_task_exist(task_name):
                print(f"Task '{task_name}' already exists.")
            else:
                create_task(task_name, importance)

        elif option == "2":
            task_name = input("Enter the task name to delete: ")

            if not does_task_exist(task_name):
                print(f"Task '{task_name}' does not exist.")
            else:
                delete_task(task_name)

        elif option == "3":
            task_name = input("Enter the task name: ")
            performance = int(input("Enter the performance for the task (0-100): "))

            if not does_task_exist(task_name):
                print(f"Task '{task_name}' does not exist.")
            else:
                set_task_performance(task_name, performance)

        elif option == "4":
            date = input("Enter the date of the task you want to display (DD-MM-YYYY): ")
            display_tasks(date)

        elif option == "5":
            date = input("Enter the date of the performance you want to get (DD-MM-YYYY): ")
            print(f"Performance on {date} is {get_performance_of_day(date)}%")

        elif option == "6":
            start_date = input("Start date: ")
            end_date = input("End date: ")
            print(f"Overall performance between {start_date} to {end_date} is {get_performance_of_a_range_of_days(start_date, end_date)}%")

        elif option == "7":
            print("Exiting the task tracker.")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()
