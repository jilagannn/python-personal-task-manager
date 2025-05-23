"""This module contains the Task Class."""

__author__ = "Jheyrus Ilagan"
__version__ = "05.19.2025"

class Task:
    """Class representing a Task from the personal task manager."""

    def __init__(self, task_name, task_description, date_due, priority="Medium",
                 status="Incomplete"):
        """Initializes a new task instance.
        
        Args:
            task_name (str): The name of specified the task.
            task_description (str): The description of the specified 
            task.
            date_due (str): The deadline date for the specified task.
            priority (str): The priority level of the specified task. 
            The default value is set to "Medium" priority.
            status (str): The overall progress of the specified task. 
            The default value is set to "Incomplete" progress.
        """

        self.task_name = task_name
        self.task_description = task_description
        self.date_due = date_due
        self.priority = priority
        self.status = status

    def __str__(self) -> str:
        """Returns the informal string representation of a Task in the 
        personal Task Manager.
        
        Returns:
            str: The informal string representation of a Task in the
        personal Task Manager.
        
        Example:
            >>> str(Task)
            Incomplete Assignment 1 (Medium - 24-01-22025)
        """

        if self.status:
            status = "Incomplete"
        else:
            status = "Completed"

        return f"{status} {self.task_name} ({self.priority} - {self.date_due})"
    
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
            "Status": self.status
        }
    
    @classmethod
    def dict_to_task(cls, task_dictionary: dict) -> str:
        """Utilizes a dictionary from a file and creates a task object.
        
        Args:
            task_dictionary (dict): A dictionary that contains the task
            object data.
        
        Return:
            str: A task object created from the dictionary.
        """

        return cls(name = task_dictionary.get("Name", "Untitled Task"),
                   description = task_dictionary.get("Description", ""),
                   date_due = task_dictionary.get("Due Date", ""),
                   priority = task_dictionary.get("Priority", "Medium"),
                   status = task_dictionary.get("Status", "Incomplete"))
    