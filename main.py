"""This module contains the main function for Personal Task Manager."""
import os
from task.task import Task
from manager.task_manager import TaskManager

__author__ = "Jheyrus Ilagan"
__version__ = "05.20.2025"

def main():
    """The main method for running the Personal Task Manager."""
    task_manager = TaskManager()
    selected_choice = ""
    while selected_choice != "5":
        selected_choice = task_manager.start_menu()
        os.system('cls' if os.name == 'nt' else 'clear')
        if selected_choice == "1":
            task_manager.view_task()
        elif selected_choice == "2":
            task_manager.add_task()
        elif selected_choice == "3":
            task_manager.update_task()
        elif selected_choice == "4":
            task_manager.delete_task()
        elif selected_choice == "5":
            print("Exiting program.")
        else:
            print("Enter a valid option.")

if __name__ == "__main__":
    main()  