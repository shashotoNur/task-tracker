"""Module containing the menu for tracking time spent"""

from utils import TASKS_LIST_FILE, does_task_exist
from utils import format_time, print_progress_bar

def add_time_to_task(task_name, time_added):
    """Function for adding time to a task"""
    task_exists = does_task_exist(task_name)

    if not task_exists:
        print(f"Task '{task_name}' does not exist.")
        return

    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line_index, line in enumerate(lines):
        if task_name in line:
            task_name, importance, current_time, target = line.split(",")

            current_time = int(current_time)
            target = int(target)

            new_time = current_time + time_added

            if new_time >= target and target != 0:
                print("Congratulations!")
                print(f"Target time {format_time(target)} has been reached!")

                target = input("Set another target in minutes ('0' to reset): ")

            updated_line = f"{task_name},{importance},{new_time},{target}\n"
            lines[line_index] = updated_line

            break

    with open(TASKS_LIST_FILE, "w", encoding="utf-8") as file:
        file.writelines(lines)

    print(f"Time added to '{task_name}' successfully.")

def display_task_times():
    """Function for displaying the time spent on a task"""
    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if len(lines) == 0:
        print("No tasks exist. Create a new task to get started.")
        return

    print("Total time invested:")

    for line in lines:
        data = line.strip().split(",")
        task_name, _, time_invested, target = data
        time_invested = int(time_invested)
        target = int(target)

        formatted_time = format_time(time_invested)
        if target != 0:
            print(f"\t- {task_name}: {formatted_time} ", end="")
            print_progress_bar((time_invested/target)*100, 20)
        else:
            print(f"\t- {task_name}: {formatted_time} ")

def time_tracker():
    """Menu for tracking collective time across tasks"""
    display_task_times()

    print("TIME TRACKER - Choose an option")
    option = input("1. Add time to a task\n2. Go back\nEnter your choice: ")

    if option == "1":
        task_name = input("Enter the task name: ")
        time_added = int(input("Enter the time to add (in minutes): "))

        add_time_to_task(task_name, time_added)

    else:
        return
