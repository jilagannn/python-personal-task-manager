"""This module contains the Task Manager Class."""

import os
from task import Task

__author__ = "Jheyrus Ilagan"
__version__ = "05.19.2025"

class TaskManager:
    """Class representing the main Task Manager program."""

    def __init__(self, filename="task-list.json"):
        """Initializes the personal Task Manager.
        
        Args:
            filename (str): The filename that the tasks will be written
            out to. Default string value will be "task-list.json
        """

        self.filename = filename
        self.tasks = []
        self.view_tasks()

    def view_tasks(self):
        """Views the list of tasks from the specified file."""
        
        for i, task in enumerate(self.tasks, 1):
            print(f"{task}")

    def add_tasks(self):
         """Adds tasks to the task list."""
         
         task_name = input("Enter the name of your task: ")
         task_description = input("Brief description of your task: ")
         due_date = input("Enter the due date (DD-MM-YYYY): ")
         priority_level = input("Determine the priority level of your task: ")

         user_task = Task(task_name, task_description, due_date, priority_level)
         self.tasks.append(user_task)


    def start_menu(self) -> str:
         """The start menu the user is greeted upon after initiating 
         the program.
         """
         start_message = "Personal Task Manager"
         border = "=" * 40
         view_task = "1. View Task"
         add_task = "2. Add Task"
         update_task = "3. Update Task"
         delete_task = "4. Delete Task"
         exit_system = "5. Exit"

         print(f"{border}\n{start_message:^40}\n\n{view_task}\n{add_task}\n{update_task}\n"
               f"{delete_task}\n{exit_system}\n{border}")
         
         return input("Select an option (1-5): ")
         