"""This module contains the Task Manager Class."""

import os
import json
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
        self.view_task()

    def view_task(self) -> None:
        """Views the list of tasks from the specified file."""
        
        for i, task in enumerate(self.tasks, 1):
            print(f"{task}")

    def load_task(self) -> None:
        """Loads the existing tasks if an external file is present."""

        if os.path.exists(self.filename):
            with open("task-list.json", "r") as file:
                file_data = json.load(file)

        else:
            self.tasks = []
    
    def add_task(self) -> None:
         """Adds tasks to the task list."""
         
         task_name = input("Enter the name of your task: ")
         task_description = input("Brief description of your task: ")
         due_date = input("Enter the due date (DD-MM-YYYY): ")
         priority_level = input("Determine the priority level of your task: ")

         user_task = Task(task_name, task_description, due_date, priority_level)
         self.tasks.append(user_task)

    def update_task(self) -> None:
        """Updates the selected task from existing task list."""

        self.view_task()
        task_selected = input("Enter the task # you would like to update: ")

    def delete_task(self):
        """Deletes a task from the task list."""

        # if not self.tasks():
        #     print("There are no tasks to delete.")
        # else:  
        self.view_task()
        border = "=" * 40
        completed_tasks = "1. Completed Tasks"
        singular_task = "2. Single Task From List"
        all_tasks = "3. All tasks"
        category_selection = input(f"{border}\n\n{completed_tasks}\n{singular_task}"
                                   f"\n{all_tasks}\n\n{border}\nSelect a category for" 
                                   f" deleting a task: ")

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

         print(f"{border}\n{start_message:^40}\n\n{view_task}\n{add_task}\n"
               f"{update_task}\n{delete_task}\n{exit_system}\n{border}")
         
         return input("Select an option (1-5): ")
         