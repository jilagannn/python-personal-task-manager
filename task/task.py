"""This module defines the Task Class."""

__author__ = "Jheyrus Ilagan"
__version__ = "05.19.2025"

class Task:
    """Class representing a Task in the personal task manager."""

    def __init__(self, task_name="Test Task", task_description="", date_due=None, 
                 priority="Medium", completed=False):
        """Initializes a new task instance.

        Args:
            task_name (str): The name of specified the task.
            task_description (str, optional): The description of the specified 
        task. The default value is set to blank.
            date_due (str, optional): The deadline date for the specified task. 
        The default value is set
            priority (str, optional): The priority level of the specified task. 
        The default value is set to "Medium" priority.
            completed (bool, optional): The overall progress of the specified task. 
        The default value is set to "False" progress.
        """

        self.task_name = task_name.strip() or "Test Task"
        self.task_description = task_description
        self.date_due = date_due
        self.priority = priority.strip().upper() or "MEDIUM"
        self.completed = completed

    def __str__(self) -> str:
        """"Returns the informal string representation of a Task in the 
        personal Task Manager.

        Returns:
            str: The informal string representation of a Task in the
        personal Task Manager.

        Example:
            >>> str(Task)
            Incomplete Assignment 1 (Medium - 24-1-2025)"""

        if self.completed:
            status = "Completed" 
        else:
            status = "Incomplete"
        if self.date_due:
            due = f"Due: {self.date_due}" 
        else:
            due = "No due date"
        return f"{status} {self.task_name} ({self.priority}) - {due}"

    def task_to_dict(self) -> dict:
        """Converts a task object into a dictionary to be utilized 
        writing and saving to a file.

        Returns:
            dict: A dictionary containing the task object.
        """

        return {
            "Name": self.task_name,
            "Description": self.task_description,
            "Due Date": self.date_due,
            "Priority Level": self.priority,
            "Status": self.completed
        }

    @classmethod
    def dict_to_task(cls, task_dictionary):
        """Utilizes a dictionary from a file and creates a task object.

        Args:
            task_dictionary (dict): A dictionary that contains the task
        object data.

        Returns:
            Task: A task object created from the dictionary.
        """
        return cls(task_name=task_dictionary.get("Name", "Untitled"),
                   task_description=task_dictionary.get("Description", ""),
                   date_due=task_dictionary.get("Due Date", ""),
                   priority=task_dictionary.get("Priority Level", "Medium"),
                   completed=task_dictionary.get("Status", False))
