import os
from termplot import Plot
from datetime import datetime, timedelta
from utils import tasks_list_file, current_month_file, print_progress_bar, format_time
from time_tracker import add_time_to_task

def get_task_relative_importance(task_name):
    importance = 0
    total_importance = 0

    with open(tasks_list_file, "r") as file:
        for line in file:
            task_data = line.strip().split(",")
            total_importance += int(task_data[1])

            if task_name in line:
                importance = int(task_data[1])

    return importance / total_importance


def update_daily_task(task_name, performance, time):
    current_date = datetime.now().strftime("%d-%m-%Y")

    with open(current_month_file, "r") as file:
        lines = file.readlines()

    new_lines = []

    task_is_to_be_written = False
    date_found = False

    line_to_be_added = f"{task_name},{performance},{time}"

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
            add_time_to_task(task_name, time)

            task_is_to_be_written = False
            print(f"Performance for task '{task_name}' set successfully.")

    if not date_found:
        new_lines.append(f"\n{current_date}\n{line_to_be_added}")
        add_time_to_task(task_name, time)

        print(f"Performance for task '{task_name}' set successfully.")

    with open(current_month_file, "w") as file:
        file.writelines(new_lines)


def display_tasks(date):
    date_object = datetime.strptime(date, "%d-%m-%Y")
    next_date_object = date_object + timedelta(days=1)

    next_date = next_date_object.strftime("%d-%m-%Y")
    found_date = False
    tasks_exist = False

    with open(current_month_file, "r") as file:
        lines = file.readlines()

    print(f"Tasks on {date}:")
    for line in lines:
        if date in line:
            found_date = True

        elif found_date:
            task_data = line.strip().split(",")
            if task_data[0] == '':
                break

            time = format_time(int(task_data[2]))
            print(f"\t- {task_data[0]} at {task_data[1]}% for {time}")
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

    return round(collective_performance, 2)

def get_performance_of_a_range_of_days(start_date, end_date):
    start_date_obj = datetime.strptime(start_date, '%d-%m-%Y')
    end_date_obj = datetime.strptime(end_date, '%d-%m-%Y')

    num_of_days = (end_date_obj - start_date_obj).days + 1
    dates, perf = [], []

    for i in range(num_of_days):
        current_date = start_date_obj + timedelta(days=i)
        dates.append(int(current_date.strftime("%d")))

    total_performance = 0

    while start_date_obj <= end_date_obj:
        performance = get_performance_of_day(start_date_obj.strftime("%d-%m-%Y"))
        perf.append(performance)
        total_performance += performance
        start_date_obj += timedelta(days=1)

    Plot(dates, perf)
    return total_performance / num_of_days

def DailyTracker():
    today = datetime.now().strftime("%d-%m-%Y")
    display_tasks(today)

    input("Press enter to continue...")

    option = input("\nDAILY TRACKER - Choose an option:\n1. Set performance and time invested for a task\n2. Get overall performance of a day\n3. Display overall performance within a date range\nEnter your choice: ")

    if option == "1":
        task_name = input("Enter the task name: ")

        performance = int(input("Enter the performance for the task (0-100): "))
        time = int(input("Enter the time invested today: "))

        update_daily_task(task_name, performance, time)

    elif option == "2":
        date = input("Enter the date of the performance you want to get (DD-MM-YYYY): ")
        performance = get_performance_of_day(date)

        print(f"Performance on {date}:")
        print_progress_bar(performance)

    elif option == "3":
        start_date = input("Start date: ")
        end_date = input("End date: ")

        performance = get_performance_of_a_range_of_days(start_date, end_date)

        print(f"Overall performance between {start_date} to {end_date}:")
        print_progress_bar(performance)

    else:
        print("Invalid option.")
