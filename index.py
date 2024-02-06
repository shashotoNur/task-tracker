"""Main module"""

import os
from manage_tasks import task_manager
from time_tracker import time_tracker
from daily_tracker import daily_tracker
from utils import TASKS_LIST_FILE, CURRENT_MONTH_FILE

def ensure_data_file_exists():
    """Function to make sure both of the files exist"""
    if not os.path.exists(TASKS_LIST_FILE):
        with open(TASKS_LIST_FILE, "a", encoding="utf-8") as file:
            file.write("")

    if not os.path.exists(CURRENT_MONTH_FILE):
        with open(CURRENT_MONTH_FILE, "w", encoding="utf-8") as file:
            file.write("")

def main():
    """Main function"""
    ensure_data_file_exists()
    first_iteration = True

    while True:
        if not first_iteration:
            input("Press enter to continue...")
        os.system('clear')

        print("MENU - Choose an option")
        print("1. Manage tasks")
        print("2. Manage collective time")
        print("3. Manage daily task")
        option = input("4. Exit\nEnter your choice: ")
        os.system('clear')

        if option == "1":
            task_manager()

        elif option == "2":
            time_tracker()

        elif option == "3":
            daily_tracker()

        elif option == "4":
            print("Program terminated...")
            break

        else:
            print("Invalid option. Please choose between 1 to 4.")

        first_iteration = False

if __name__ == "__main__":
    main()
