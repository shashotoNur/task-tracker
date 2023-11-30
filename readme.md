# Task Tracker

Task Tracker is a Python-based command line application designed to help users manage tasks, track time invested, and evaluate task performances. It provides a simple and intuitive command-line interface for various task-related operations.

## Table of Contents

- [Task Tracker](#task-tracker)
  - [Table of Contents](#table-of-contents)
  - [Files](#files)
  - [Usage](#usage)
  - [Prerequisites](#prerequisites)
  - [How to Clone](#how-to-clone)
  - [About](#about)
    - [Why it is Useful](#why-it-is-useful)
  - [License](#license)
  - [Contributor](#contributor)

## Files

1. **index.py**
   - The main file orchestrating the program flow with a menu for task management, total time tracking, and daily task evaluations
2. **manage_tasks.py**
   - Functions for creating, deleting, editing tasks, and listing all tasks.
   - Invoked through the main menu option "1. Manage tasks" in `index.py`.

3. **time_tracker.py**
   - Functionality for adding time to tasks and displaying time invested.
   - Invoked through the main menu option "2. Manage collective time" in `index.py`.

4. **daily_tracker.py**
   - Supports setting and displaying task performances and time invested on current date.
   - Calculates overall performance for a day and within a specified date range.
   - Invoked through the main menu option "3. Manage tasks" in `index.py`.

5. **utils.py**
   - Utility functions shared across multiple files.
   - Manages task and performance data files, checks for task existence, and formats time.
   - Provides functions for printing tables and progress bars.

## Usage

To run the program, execute `index.py`. Follow the on-screen menu to manage tasks, track time, and evaluate performances.

Make sure to check the `tasks_list.txt` file for task data and the `tasks_in_<current_year>_<current_month>.txt` file for performance data.

## Prerequisites

- Python 3.x installed on your machine.

## How to Clone

```bash
git clone https://github.com/shashotoNur/task-tracker.git
cd task-tracker
python index.py
```

## About

Task Tracker simplifies task management, time tracking, and performance evaluation in a single, easy-to-use Python application. It provides a seamless command-line interface, making it suitable for personal productivity tracking or small project management.

### Why it is Useful

- **Task Management:** Create, delete, edit, and list tasks effortlessly.
- **Time Tracking:** Track time invested in each task.
- **Daily Tasks Evaluation:** Evaluate task performances and time invested on a daily or overall basis.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributor

- [**Shashoto Nur**](https://github.com/shashotoNur)
