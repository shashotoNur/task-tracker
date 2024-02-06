"""Module containing the menu for daily tasks"""

import os
from datetime import datetime, timedelta

import plotext as plt
from utils import TASKS_LIST_FILE, CURRENT_MONTH_FILE, format_time
from time_tracker import add_time_to_task
from manage_tasks import list_all_tasks

def get_task_relative_importance(task_name):
    """Function for getting the importance of a task relative to other tasks"""
    importance = 0
    total_importance = 0

    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        for line in file:
            task_data = line.strip().split(",")
            total_importance += int(task_data[1])

            if task_name in line:
                importance = int(task_data[1])

    return importance / total_importance


def update_daily_task(task_name, performance, time):
    """Function for updating the performance and time of current day's task"""
    current_date = datetime.now().strftime("%d-%m-%Y")

    with open(CURRENT_MONTH_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    new_lines = []

    task_is_to_be_written = False
    date_found = False

    line_to_be_added = f"{task_name},{performance},{time}"

    for line_number, line in enumerate(lines):
        new_lines.append(line)
        task_in_line = line.strip().split(",")[0]

        if current_date in line:
            task_is_to_be_written = True
            date_found = True

        elif task_is_to_be_written and task_name == task_in_line:
            print(f"Performance for today's '{task_name}' is already set.")
            task_is_to_be_written = False

        elif task_is_to_be_written and line_number == (len(lines)-1):
            new_lines.append(f"\n{line_to_be_added}")
            add_time_to_task(task_name, time)

            task_is_to_be_written = False
            print(f"Performance for task '{task_name}' set successfully.")

    if not date_found:
        new_lines.append(f"\n{current_date}\n{line_to_be_added}")
        add_time_to_task(task_name, time)

        print(f"Performance for task '{task_name}' set successfully.")

    with open(CURRENT_MONTH_FILE, "w", encoding="utf-8") as file:
        file.writelines(new_lines)


def display_tasks(date):
    """Function displaying all the tasks on a particular date"""
    date_object = datetime.strptime(date, "%d-%m-%Y")
    next_date_object = date_object + timedelta(days=1)

    next_date = next_date_object.strftime("%d-%m-%Y")
    found_date = False
    tasks_exist = False

    year = date[6:]
    month = date[3:5]
    filename = f"tasks_in_{year}_{month}.txt"
    if not os.path.exists(filename):
        return print(f"No record on {date} exists.")

    with open(filename, "r", encoding="utf-8") as file:
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
        return print(f"No tasks on {date}.")
    return print("---")

def get_performance_of_day(date):
    """Function for getting the overall performance on a day"""
    found_date = False
    collective_performance = 0

    year = date[6:]
    month = date[3:5]
    filename = f"tasks_in_{year}_{month}.txt"
    if not os.path.exists(filename):
        return 0

    with open(filename, "r", encoding="utf-8") as file:
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
    """Function for getting the overall performance of a number of days"""
    start_date_obj = datetime.strptime(start_date, '%d-%m-%Y')
    end_date_obj = datetime.strptime(end_date, '%d-%m-%Y')

    num_of_days = (end_date_obj - start_date_obj).days + 1
    dates, performances = [], []

    for i in range(num_of_days):
        current_date = start_date_obj + timedelta(days=i)
        dates.append(current_date.strftime("%d/%m"))

    total_performance = 0

    while start_date_obj <= end_date_obj:
        performance = get_performance_of_day(start_date_obj.strftime("%d-%m-%Y"))
        performances.append(performance)
        total_performance += performance
        start_date_obj += timedelta(days=1)

    if not all(x == 0 for x in performances):
        plt.simple_bar(dates, performances, width = 100, title = 'Performance Bar')
        plt.show()
    return total_performance / num_of_days

def daily_tracker():
    """Menu for daily tasks"""
    today = datetime.now().strftime("%d-%m-%Y")
    display_tasks(today)

    print("DAILY TRACKER - Choose an option:")
    print("1. Set performance and time invested for a task")
    print("2. Display tasks on a date")
    print("3. Get overall performance of a day")
    print("4. Display overall performance within a date range")
    option = input("5. Go back\nEnter your choice: ")

    if option == "1":
        list_all_tasks()
        task_name = input("Enter the task name: ")

        performance = int(input("Enter the performance for the task (0-100): "))
        time = int(input("Enter the time invested today in minutes: "))

        update_daily_task(task_name, performance, time)

    elif option == "2":
        date = input("Enter the date you want to view (DD-MM-YYYY): ")
        display_tasks(date)

    elif option == "3":
        date = input("Enter the date of the performance you want to get (DD-MM-YYYY): ")
        performance = get_performance_of_day(date)

        plt.simple_bar([f"On {date}"], [performance], width = 100, title = 'Overall Performance')
        plt.show()

    elif option == "4":
        start_date = input("Start date (DD-MM-YYYY): ")
        end_date = input("End date (DD-MM-YYYY): ")

        performance = get_performance_of_a_range_of_days(start_date, end_date)

        plt.simple_bar([f"{start_date} to {end_date}"], [performance], width = 100, title = 'Overall Performance')
        plt.show()

    else:
        return
