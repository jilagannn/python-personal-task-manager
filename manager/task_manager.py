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
        self.load_task()

    def view_task(self) -> None:
        """Views the list of tasks from the specified file."""
        if self.tasks:
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
        else:
             print("There are no tasks.")

        input("\nPress enter to return to menu selection. ")

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
            json.dump(saved_data, file, indent=2)

    
    def add_task(self) -> None:
         """Adds tasks to the task list."""
         
         task_name = input("Enter the name of your task: ")
         task_description = input("Brief description of your task: ")
         due_date = input("Enter the due date (DD-MM-YYYY): ")
         priority_level = input("Determine the priority level of your task: ")

         user_task = Task(task_name, task_description, due_date, priority_level)
         self.tasks.append(user_task)
         self.save_task()

    def update_task(self) -> None:
        """Updates the selected task from existing task list."""

        if self.tasks:
            border = "=" * 40
            update_task_title = "Update Task Components"
            name_option = "1. Name"
            description_option = "2. Description"
            due_date_option = "3. Due Date"
            priority_level_option = "4. Priority Level"
            status_option = "5. Status"
            menu_exit = "6. Exit"
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")
            print(border)
            user_input = int(input("Enter the task " \
            "# you would like to update: "))
            print(border)
            task_list = user_input - 1
            desired_task = self.tasks[task_list]
            print (desired_task)
            menu_selection = ""
            while menu_selection != 6:
                print(f"{border}\n{update_task_title:^40}\n\n{name_option}\n{description_option}\n{due_date_option}"
                      f"\n{priority_level_option}\n{status_option}\n{menu_exit}\n")
                menu_selection = int(input("Which field of the task did you want to update?: "))
                if menu_selection == 1:
                    updated_name = input("\nEnter the desired task name: ")
                    desired_task.task_name = updated_name
                elif menu_selection == 2:
                    updated_description = input("\nEnter the new description for your " \
                    "task: ")
                    desired_task.task_description = updated_description
                    print(f"{border}\nTask description has been updated.")
                elif menu_selection == 3:
                    updated_due_date = input("\nEnter the new due date for your task "
                    "in the following format DD-MM-YYYY: ")
                    desired_task.date_due = updated_due_date
                    print(f"{border}\nTask due date has been updated.")
                elif menu_selection == 4:
                    updated_priority_level = input("\nDetermine the new priority level " \
                    "for your task: ").upper()
                    desired_task.priority = updated_priority_level
                    print(f"{border}\nTask priority level has been updated.")
                elif menu_selection == 5:
                    updated_status = input("\nIs your task completed? " \
                    "Enter y/n: ").lower()
                    if updated_status == "y":
                        updated_status = True
                        print(f"{border}\nTask has been marked as complete.")
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
            self.tasks
            border = "=" * 40
            finished_tasks = "1. Completed Tasks"
            singular_task = "2. Single Task From List"
            all_tasks = "3. All tasks"
            return_to_main_menu = "4. Exit"
            category_selection = 1111
            while category_selection != 4:
                category_selection = int(input(f"{border}\n\n{finished_tasks}\n"
                                            f"{singular_task}\n{all_tasks}\n{return_to_main_menu}"
                                            f"\n\n{border}\nSelect a category by " 
                                            f"inputting the corresponding "
                                            f"number: "))
                if category_selection == 1:
                    completed_task = []
                    for task in self.tasks:
                        if task.completed == True:
                            task_position = self.tasks.index(task)
                            completed_task.append(task_position)
                    if not completed_task:
                         print("There are no completed tasks.")
                    else:
                        print(border)
                        for number, i in enumerate(completed_task, 1):
                            print(f"{number}. {self.tasks[i]}")
                        print(border)
                        selected_option = int(input("1. Delete all completed tasks"
                                                    "\n2. Delete selected completed task\n3. Exit\n"
                                                    "Select an action: "))
                        if selected_option == 1:
                            incomplete_task = []
                            for task in self.tasks:
                                if task.completed != True:
                                    incomplete_task.append(task)
                            confirmation_prompt = ""
                            while confirmation_prompt != "n" and confirmation_prompt != "y":
                                    confirmation_prompt = input("Are you sure you want to delete all " \
                                    "completed tasks? \nEnter y/n: ").lower()
                                    if confirmation_prompt not in ("y", "n"):
                                        print("Please enter confirmation.")
                            if confirmation_prompt == "y":
                                    print("Deleting all completed tasks.")
                                    self.tasks = incomplete_task
                                    print("All completed tasks have been deleted.")
                                    self.save_task()
                                    print("Returning to selection.")
                            else:
                                print("Returning to selection.")
                        elif selected_option == 2:
                            selected_task = int(input("Select which completed task to delete:"))
                            confirmation_prompt = ""
                            while confirmation_prompt != "n" and confirmation_prompt != "y":
                                    confirmation_prompt = input("Are you sure you want to delete this " \
                                    "task?\nEnter y/n: ").lower()
                                    if confirmation_prompt not in ("y", "n"):
                                        print("Please enter confirmation.")
                            if confirmation_prompt == "y":
                                print("Deleting completed task.")
                                self.tasks.pop(completed_task[selected_task - 1])
                                print("Completed task has been deleted.")
                                self.save_task()
                                print("Returning to selection.")
                            else:
                                print("Returning to selection.")
                elif category_selection == 2:
                    for index, task in enumerate(self.tasks, 1):
                        print(f"{index}. {task}")
                    chosen_task = int(input("Enter the corresponding # of the task you would" \
                    "like to delete: "))
                    task_index = chosen_task - 1
                    confirmation_prompt = ""
                    while confirmation_prompt != "n" and confirmation_prompt != "y":
                        confirmation_prompt = input("Are you sure you want to delete selected task? " \
                        "Enter y/n: ").lower()
                        if confirmation_prompt not in ("y", "n"):
                                    print("Please enter confirmation.")
                    if confirmation_prompt == "y":
                        print("Deleting task.")
                        self.tasks.pop(task_index)
                        print("Task has been successfully deleted.")
                        self.save_task()
                    else:
                        print("Returning to selection.")
                elif category_selection == 3:
                    user_choice = ""
                    while user_choice != "n" and user_choice != "y":
                        user_choice = input("Are you sure you want to delete all tasks? Enter y/n: ").lower()
                        if user_choice not in ("y", "n"):
                                    print("Please enter confirmation.")
                    if user_choice == "y":
                        self.tasks.clear()
                        print("Deleting all tasks.")
                        self.save_task()
                        print("Tasks have been successfully deleted.")
                    else:
                         print("Returning to selection.")
                else:
                    self.save_task()
                    print("Exiting task delete menu.")

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
               f"{update_task}\n{delete_task}\n{exit_system}\n\n{border}")
         
         return input("Select an option (1-5): ")
         