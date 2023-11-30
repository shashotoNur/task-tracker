import os
from manage_tasks import TaskManager
from time_tracker import TimeTracker
from daily_tracker import DailyTracker
from utils import tasks_list_file, current_month_file

def ensure_data_file_exists():
    if not os.path.exists(tasks_list_file):
        with open(tasks_list_file, "a") as file:
            file.write("")

    if not os.path.exists(current_month_file):
        with open(current_month_file, "w") as file:
            file.write("")

def main():
	ensure_data_file_exists()
	first_iteration = True

	while True:
		if not first_iteration:
			input("Press enter to continue...")

		option = input("\nMENU - Choose an option\n1. Manage tasks\n2. Manage collective time\n3. Manage daily task\n4. Exit\nEnter your choice: ")

		if option == "1":
			TaskManager()

		elif option == "2":
			TimeTracker()

		elif option == "3":
			DailyTracker()

		elif option == "4":
			print("Program terminated...")
			break

		else:
			print("Invalid option. Please choose between 1 to 4.")

		first_iteration = False

if __name__ == "__main__":
    main()
