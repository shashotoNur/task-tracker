"""Module containing useful functions"""

from datetime import datetime

TASKS_LIST_FILE = "tasks_list.txt"
CURRENT_MONTH_FILE = f"tasks_in_{datetime.now().strftime('%Y_%m')}.txt"

def does_task_exist(task_name):
    """Checks whether a task actually exists"""
    with open(TASKS_LIST_FILE, "r", encoding="utf-8") as file:
        lines = file.readlines()

    for line in lines:
        if task_name in line:
            return True

    return False

def format_time(time_in_minutes):
    """Creates a readable time from minutes"""
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60

    formatted_time = ""

    if hours > 0:
        formatted_time += f"{hours} hours, "

    formatted_time += f"{minutes} minutes"
    return formatted_time

def print_table(table_data):
    """Creates a table to print data"""
    column_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]

    title_row = "|".join(f"{{:{width}}}" for width in column_widths)
    print(title_row.format(*table_data[0]))

    separator_line = "+".join("-" * width for width in column_widths)
    print(separator_line)

    for row in table_data[1:]:
        row_str = "|".join(f"{{:{width}}}" for width in column_widths)
        print(row_str.format(*row))

def print_progress_bar(progress, length=40):
    """Prints a progress bar"""
    bar_length = int(length * progress/100)
    bars = "=" * bar_length + "." * (length - bar_length)

    print(f"[{bars}] {progress:.2f}%")
