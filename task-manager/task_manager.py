"""This module contains the Task Manager Class."""

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
