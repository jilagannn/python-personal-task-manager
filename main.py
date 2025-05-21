"""This module contains the main function for Personal Task Manager."""

from task.task import Task
from manager.task_manager import TaskManager

__author__ = "Jheyrus Ilagan"
__version__ = "05.20.2025"

def main():
    """The main method for running the Personal Task Manager."""
    task_manager = TaskManager()
    task_manager.start_menu()

if __name__ == "__main__":
    main()