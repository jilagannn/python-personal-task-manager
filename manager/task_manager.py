"""This module contains the Task Manager Class."""

__author__ = "Jheyrus Ilagan"
__version__ = "05.19.2025"

import os
import time
import json
from task.task import Task

class TaskManager:
    """Class representing the main Task Manager program."""

    def __init__(self, filename: str="task-list.json"):
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

        border = "=" * 80
        if self.tasks:
            task_list_title = "My Tasks"
            print(f"{border}\n{task_list_title:^80}\n{border}")
            for index, task in enumerate(self.tasks, 1):
                print(f"\n{index}. {task}\n")
            print(border)
        else:
             print(f"{border}\nThere are no tasks.")

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

        border = "=" * 80
        add_task_message = "Add Task"
        print(f"{border}\n{add_task_message:^80}\n{border}")
        task_name = input("Enter the name of your task: ")
        task_description = input("Brief description of your task: ")
        due_date = input("Enter the due date (DD-MM-YYYY): ")
        priority_level = input("Determine the priority level of your task: ")
        user_task = Task(task_name, task_description, due_date, priority_level)
        self.tasks.append(user_task)
        print(f"{border}\nTask has been added successfully! \nReturning to menu select.")
        self.save_task()

    def display_task_list(self, title: str="Tasks") -> None:
        """Displays the current task list for the user."""

        border = "=" * 80
        print(f"{border}\n{title:^80}\n{border}")
        for index, task in enumerate(self.tasks, 1):
            print(f"\n{index}. {task}\n")
        print(border)

    def update_task(self) -> None:
        """Updates the selected task from existing task list."""

        if not (self.tasks):
             print("No tasks to update. Please add a task first!")

        else:
             selected_task = self.select_task_to_update()
             print(selected_task)
             self.update_task_field(selected_task)
             self.save_task()
             print("Exiting task update menu.")

    def select_task_to_update(self) -> Task:
        """Acquires the selected task to be updated.
        
        Returns:
            Task: Task object selected from the list.
        """
        
        self.display_task_list(title="Update Task")
        user_input = int(input("Enter the task # you would like to update: "))
        print("=" * 80)
        task_list = user_input - 1
        desired_task = self.tasks[task_list]
        
        return desired_task
    
    def display_and_select_update_menu_option(self) -> int:
        """Displays the task components available for update.
        
        Returns:
            int: The field of the task to be updated.
        """

        border = "=" *80
        component_title = "Update Task Components"
        name_option = "1. Name"
        description_option = "2. Description"
        due_date_option = "3. Due Date"
        priority_level_option = "4. Priority Level"
        status_option = "5. Status"
        menu_exit = "6. Exit"

        print(f"{border}\n{component_title:^80}\n\n{name_option}\n{description_option}"
              f"\n{due_date_option}\n{priority_level_option}\n{status_option}\n{menu_exit}\n")
        selected_field = int(input("Which field of the task did you want to update?: "))

        return selected_field
    
    def update_single_field_of_task(self, task: Task, field: int) -> None:
        """Updates a single field of a task."""

        border = "=" * 80
        if field == 1:
                    updated_name = input(f"{border}\nEnter the desired task name: ")
                    task.task_name = updated_name
                    print(f"{border}\nTask name has been updated.")

        elif field == 2:
            updated_description = input(f"{border}\nEnter the new description for your " \
            "task: ")
            task.task_description = updated_description
            print(f"{border}\nTask description has been updated.")

        elif field == 3:
            updated_due_date = input(f"{border}\nEnter the new due date for your task "
            "in the following format DD-MM-YYYY: ")
            task.date_due = updated_due_date
            print(f"{border}\nTask due date has been updated.")

        elif field == 4:
            updated_priority_level = input(f"{border}\nDetermine the new priority level " \
            "for your task: ").upper().strip()

            if updated_priority_level == "":
                 task.priority = "Medium"
                 print(f"{border}\nTask priority level has been updated.")

            else:
                task.priority = updated_priority_level
                print(f"{border}\nTask priority level has been updated.")

        elif field == 5:
            updated_status = input(f"{border}\nIs your task completed? " \
            "\nEnter y/n: ").lower()

            if updated_status == "y":
                updated_status = True
                print(f"{border}\nTask has been marked as complete.")
            
            else:
                updated_status = False

            task.completed = updated_status
        time.sleep(2)

    def update_task_field(self, task: Task) -> None:
        """Updates the selected field of the task."""

        menu_selection = ""
        while menu_selection != 6:
            menu_selection =  self.display_and_select_update_menu_option()
            if menu_selection in range(1, 6):
                 self.update_single_field_of_task(task, menu_selection)

    def delete_task(self):
        """Deletes selected task(s) from existing task."""

        if not self.tasks:
            print("There are no tasks to delete.")

        else:
            category_selection = 1111

            while category_selection != 4:
                category_selection = self.display_and_select_delete_menu_option()
                
                if category_selection ==1:
                    self.completed_task_deletion()
                
                elif category_selection ==2:
                    self.single_task_deletion()

                elif category_selection ==3:
                    self.all_tasks_deletion()
                
                if not self.tasks:
                    print("There are no more tasks to delete.")
                    time.sleep(2)
                    break

            print("Exiting task delete menu.")

    def  confirmation_prompt(self, message_prompt: str):
        """Acquires the confirmation from the user when executing a task.
        
        Args:
            message_prompt (str): The confirmation prompt from the user.

        Returns:
            bool: True if user confirms with "y", False if user confirms with "n".
        """

        confirmation_prompt = ""
        while confirmation_prompt != "n" and confirmation_prompt != "y":
                confirmation_prompt = input(f"{message_prompt} \nEnter y/n: ").lower()
                if confirmation_prompt not in ("y", "n"):
                    print("Please enter confirmation.")

        return confirmation_prompt == "y"
    
    def display_and_select_delete_menu_option(self) -> int:
        """Displays the menu for which category of tasks to delete from.
        
        Returns:
            int: The category the user has selected.
        """

        border = "=" * 80
        delete_title = "Delete Task(s)"
        finished_tasks = "1. Completed Tasks"
        singular_task = "2. Single Task From List"
        all_tasks = "3. All tasks"
        return_to_main_menu = "4. Exit"
        category_selection = int(input(f"{border}\n{delete_title:^80}\n{border}\n"
                                f"\n{finished_tasks}\n{singular_task}\n{all_tasks}\n"
                                f"{return_to_main_menu}\n\n{border}"
                                f"\nSelect a category by inputting the "
                                f"corresponding number: "))
        
        return category_selection
    
    def completed_task_deletion(self):
        """Main method for handling the deletion of completed tasks."""

        completed_tasks = self.acquire_completed_tasks()
        if completed_tasks:
            self.display_completed_task_list(completed_tasks)
            user_action = self.display_and_select_completed_tasks_deletion_menu()
           
            if user_action == 1:
                self.delete_all_completed_tasks()
           
            elif user_action ==2:
                self.delete_selected_completed_task(completed_tasks)
            
            elif user_action == 3:
                 print("Returning to selection")
                 time.sleep(2)
        
        else:
            print("There are no completed tasks.")

    def acquire_completed_tasks(self) -> list:
        """Acquires the completed tasks and adds them onto a new list.
        
        Returns:
            list: The list of completed tasks.
        """

        completed_task = []
        for task in self.tasks:
            if task.completed == True:
                task_position = self.tasks.index(task)
                completed_task.append(task_position)

        return completed_task
    
    def display_and_select_completed_tasks_deletion_menu(self) -> int:
        """Displays the menu for which method to delete completed tasks.
        
        Returns:
            int: The method the user has selected."""
        
        border = "=" * 80
        selected_option = int(input(f"\n1. Delete all completed tasks"
                                                    "\n2. Delete selected completed task\n3. Exit\n"
                                                    f"\n{border}\nSelect an action: "))
        
        return selected_option
    
    def display_completed_task_list(self, completed_list: list, title: str="Completed Tasks"):
        """Displays a list of completed tasks.
        
        Args:
            completed_list (list): The list for completed tasks.
            title (str): The title displaying the list.
        """

        border = "=" * 80
        print(f"{border}\n{title:^80}\n{border}")
        for number, i in enumerate(completed_list, 1):
            print(f"\n{number}. {self.tasks[i]}\n")
        print(border)

    def delete_all_completed_tasks(self):
        """Deletes all the completed tasks."""

        border = "=" * 80
        incomplete_task = []
        for task in self.tasks:
            if not task.completed:
                incomplete_task.append(task)
        prompt = self.confirmation_prompt("Would you like to delete all completed tasks?")
        
        if  prompt:
            print(f"{border}\nDeleting all completed task.")
            self.tasks = incomplete_task
            print(f"{border}\nAll completed tasks have been deleted.")
            self.save_task()
            print("Returning to selection.")
        
        else:
            print("Returning to selection.")

        time.sleep(2)

    def delete_selected_completed_task(self, completed_list):
        """Deletes the selected completed task from the task list.
        
        Args:
            completed_list (list): The list of completed tasks.
        """

        border = "=" * 80
        self.display_completed_task_list(completed_list)
        chosen_task = int(input("Enter the corresponding # of the task you would " \
                        "like to delete: "))
        task_index = chosen_task - 1
        completed_task = completed_list[task_index]
        prompt = self.confirmation_prompt("Are you sure you want to delete selected task?")
        
        if prompt:
            print(f"{border}\nDeleting task.")
            self.tasks.pop(completed_task)
            print(f"{border}\nTask has been successfully deleted. \nReturning to "
                    f"selection.")
            self.save_task()
        
        else:
            print("Returning to selection.")
        
        time.sleep(2)

    def single_task_deletion(self):
        """Main method for deleting a single task from the task list."""

        border = "=" * 80
        self.display_task_list(title="My Tasks")
        user_choice = int(input("Enter the corresponding # of the task you would " \
                                "like to delete: "))
        task_index = user_choice - 1
        prompt = self.confirmation_prompt("Are you sure you want to delete the " \
                                            "selected task?")
        
        if prompt:
            print(f"{border}\nDeleting task.")
            self.tasks.pop(task_index)
            print(f"{border}\nTask has been successfully deleted. \nReturning to "
                f"selection.")
            self.save_task()
        
        else:
            print("Returning to selection.")
        
        time.sleep(2)
    
    def all_tasks_deletion(self):
        """Main method for deleting all tasks from the task list."""

        border = "=" * 80
        self.display_task_list(title="My Tasks")
        prompt = self.confirmation_prompt("Are you sure you want to delete all tasks?")
        
        if prompt:
            print(f"{border}\nDeleting all tasks.")
            self.tasks.clear()
            print(f"{border}\nAll tasks have been successfully deleted. \nReturning to "
                f"selection.")
            self.save_task()
        
        else:
            print("Returning to selection.")

        time.sleep(2)

    def start_menu(self) -> str:
        """The start menu the user is greeted upon after initiating the program."""
        
        start_message = "Personal Task Manager"
        border = "=" * 80
        view_task = "1. View Task"
        add_task = "2. Add Task"
        update_task = "3. Update Task"
        delete_task = "4. Delete Task"
        exit_system = "5. Exit"

        print(f"{border}\n{start_message:^80}\n\n{view_task}\n{add_task}\n"
            f"{update_task}\n{delete_task}\n{exit_system}\n\n{border}")

        return input("Select an option (1-5): ")
         