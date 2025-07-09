"""This module contains the Task Manager Class."""

import os
import json
from task.task import Task

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
            with open(self.filename, "r") as file:
                file_data = json.load(file)
                for data in file_data:
                    task = Task.dict_to_task(data)
                    self.tasks.append(task)

        else:
            self.tasks = []

    def save_task(self) -> None:
        "Saves current task into a dictionary onto an external file."

        with open(self.filename, "w") as file:
            saved_data = []
            for task_object in self.tasks:
                task_dictionary = task_object.task_to_dict()
                saved_data.append(task_dictionary)
            json.dump(saved_data, file)

    
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

        if self.tasks:
            user_input = int(input("Enter the task " \
            "# you would like to update: "))
            task_list = user_input - 1
            desired_task = self.tasks[task_list]
            print (desired_task)
            menu_selection = ""
            while menu_selection != 6:
                menu_selection = int(input("Which field of the task "  
                                   "did you want to update?\n1. Name\n"
                                   "2. Description\n3. Due Date\n"
                                   "4. Priority Level\n5. Status\n6. Exit"))
                if menu_selection == 1:
                    updated_name = input("Enter the desired task name:")
                    desired_task.task_name = updated_name
                elif menu_selection == 2:
                    updated_description = input("Enter the new description for your " \
                    "task:")
                    desired_task.task_description = updated_description
                elif menu_selection == 3:
                    updated_due_date = input("Enter the new due date for your task "
                    "in the following format DD-MM-YYYY:")
                    desired_task.date_due = updated_due_date
                elif menu_selection == 4:
                    updated_priority_level = input("Determine the new priority level" \
                    "for your task:")
                    desired_task.priority = updated_priority_level
                elif menu_selection == 5:
                    updated_status = input("Is your task completed? " \
                    "Enter y/n:").lower()
                    if updated_status == "y":
                        updated_status = True
                    else:
                        updated_status = False
                    desired_task.completed = updated_status
                
            else:
                self.save_task()
                print("Exiting task update menu.")
        
        else:
            print("No tasks to update. Please add a task first!")

    def delete_task(self):
        """Deletes a task from the task list."""

        if not self.tasks:
            print("There are no tasks to delete.")
        else:  
            self.view_task()
            border = "=" * 40
            completed_tasks = "1. Completed Tasks"
            singular_task = "2. Single Task From List"
            all_tasks = "3. All tasks"
            category_selection = int(input(f"{border}\n\n{completed_tasks}\n"
                                           f"{singular_task}\n{all_tasks}\n\n"
                                           f"{border}\nSelect a category by " 
                                           f"inputting the corresponding "
                                           f"number: "))

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
         