from datetime import datetime

tasks_list_file = "tasks_list.txt"
current_month_file = f"tasks_in_{datetime.now().strftime('%Y_%m')}.txt"

def does_task_exist(task_name):
    with open(tasks_list_file, "r") as file:
        lines = file.readlines()

    for line in lines:
        if task_name in line:
            return True

    return False

def format_time(time_in_minutes):
    hours = time_in_minutes // 60
    minutes = time_in_minutes % 60

    formatted_time = ""

    if hours > 0:
        formatted_time += f"{hours} hours, "

    formatted_time += f"{minutes} minutes"
    return formatted_time

def print_table(table_data):
    column_widths = [max(len(str(item)) for item in col) for col in zip(*table_data)]

    title_row = "|".join(f"{{:{width}}}" for width in column_widths)
    print(title_row.format(*table_data[0]))

    separator_line = "+".join("-" * width for width in column_widths)
    print(separator_line)

    for row in table_data[1:]:
        row_str = "|".join(f"{{:{width}}}" for width in column_widths)
        print(row_str.format(*row))

def print_progress_bar(progress, length=40):
    bar_length = int(length * progress/100)
    bar = "=" * bar_length + "." * (length - bar_length)

    print(f"[{bar}] {progress:.2f}%")
