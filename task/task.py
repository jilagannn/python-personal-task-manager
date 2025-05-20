"""This module contains the Task Class."""

__author__ = "Jheyrus Ilagan"
__version__ = "05.19.2025"

class Task:
    """Class representing a Task from the personal task manager."""

    def __init__(self, task_name, task_description, date_due, priority, status):
        """Initializes a new task instance.
        
        Args:
            task_name (str): The name of specified the task.
            task_description (str): The description of the specified 
            task.
            date_due (str): The deadline date for the specified task.
            priority (str): The priority level of the specified task.
            status (str): The overall progress of the specified task.
        """

        self.task_name = task_name
        self.task_description = task_description
        self.date_due = date_due
        self.priority = priority
        self.status = status