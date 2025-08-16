"""This modules defines the test cases for the Task Manager class.

Test Cases:
    view_task()
    - Verifies if the task list is empty.
"""

import unittest
import json
from unittest.mock import patch
from io import StringIO
from unittest import TestCase
from task.task import Task
from manager.task_manager import TaskManager

__author__ = "Jheyrus Ilagan"
__version__ = "10.14.2025"

class TestTaskManager(TestCase):
    """Defines the unit tests for Task Manager class."""

    def setUp(self):
        """This function is called before executing a unit test function.
        
        The following class objects have been provided to reduce the amount of code needed
        when creating Task Manager class objects in the following tests.
        
        Example:
            >>>task_manager = TaskManager(self.tasks)
        """

        self.test_tasks = [
            {
                "Name": "Test Task",
                "Description": "Test task object",
                "Due Date": "01-24-2026",
                "Priority Level": "LOW",
                "Status": False
            },
            {
                "Name": "",
                "Description": "",
                "Due Date": "",
                "Priority Level": "",
                "Status": False
            },
            {
                "Name": "",
                "Description": "",
                "Due Date": "",
                "Priority Level": "",
                "Status": False
            },
            {
                "Name": "",
                "Description": "",
                "Due Date": "",
                "Priority Level": "",
                "Status": False
            },
            {
                "Name": "",
                "Description": "",
                "Due Date": "",
                "Priority Level": "",
                "Status": False
            },
        ]

        self.empty_task_list = "empty-test-task-list.json"
        with open(self.empty_task_list, "w") as file:
            json.dump([], file, indent=2)

    ### view_task()

    def test_view_task_if_task_list_empty(self):
        # Arrange
        task_manager = TaskManager(self.empty_task_list)
        user_input = ""

        # Act
        with patch("builtins.input", return_value=user_input), \
        patch('sys.stdout', new=StringIO()) as fake_out:
            actual_return = task_manager.view_task()
            actual_message = fake_out.getvalue()

        # Assert
        expected_view_task_return = None
        expected_message = "=" * 40 + "\nThere are no tasks.\n"
        self.assertEqual(expected_view_task_return, actual_return)
        self.assertEqual(expected_message, actual_message)