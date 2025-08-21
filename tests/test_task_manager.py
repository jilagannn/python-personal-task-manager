"""This modules defines the test cases for the Task Manager class.

Test Cases:
    view_task()
    - Verifies if the task list is empty.
    - Verifies if task list contains the correct number of task entries.
    - Verifies if task is being outputted correctly.

    load_task()
    - Task list is empty if non existent file is loaded.
    - Verifies that the correct number of Task objects are loaded.
    - Verifies data is properly converted into Task objects.

    save_task()
    - Task list is saved properly even if file is empty.
    - Task list properly saves correct quantity of tasks onto file.
    - Saved tasks contain correct data after saving.

    add_task()
    - Tasks are successfully added as task objects.
"""

import unittest
import json
import os
from unittest.mock import patch
from unittest.mock import Mock
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

        self.tasks_test = []
        self.test_task_list = 'test-task-list.json'
        self.test_tasks = [
            {
                "Name": "Test Task",
                "Description": "Test task object",
                "Due Date": "01-24-2026",
                "Priority Level": "Low",
                "Status": False
            },
            {
                "Name": "Test Task 2",
                "Description": "Second test task.",
                "Due Date": "02-24-2026",
                "Priority Level": "Low",
                "Status": False
            },
            {
                "Name": "Mow Lawn",
                "Description": "Chore for the weekend.",
                "Due Date": "10-24-2025",
                "Priority Level": "Medium",
                "Status": False
            },
            {
                "Name": "Trade",
                "Description": "Crypto trade quota.",
                "Due Date": "12-30-2025",
                "Priority Level": "High",
                "Status": False
            },
            {
                "Name": "Test Task 3",
                "Description": "Third test task.",
                "Due Date": "03-20-2026",
                "Priority Level": "Low",
                "Status": False
            },
        ]
        with open(self.test_task_list, "w") as output_file:
            json.dump(self.test_tasks, output_file, indent=2)

        self.empty_task_list = "empty-test-task-list.json"
        with open(self.empty_task_list, "w") as file:
            json.dump([], file, indent=2)
        
        self.empty_task_list_save = "empty-test-task-list_saved.json"   
        with open(self.empty_task_list_save, "w") as file:
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

    def test_view_task_if_task_list_outputs_correct_task(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)
        user_input = ""

        # Act
        with patch("builtins.input", return_value=user_input), \
        patch('sys.stdout', new=StringIO()) as fake_out:
            actual_return = task_manager.view_task()
            actual_message = fake_out.getvalue()

        # Assert
        expected_task_return = None
        expected_message = "1. Incomplete Test Task (Low) - Due: 01-24-2026"
        self.assertEqual(expected_task_return, actual_return)
        self.assertIn(expected_message, actual_message)

    def test_view_task_if_task_list_contains_correct_number_of_tasks(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)
        user_input = ""
        actual_count = 0

        # Act
        with patch("builtins.input", return_value=user_input), \
        patch('sys.stdout', new=StringIO()) as fake_out:
            actual_return = task_manager.view_task()
            mocked_output = fake_out.getvalue()
        for task_number in range(1, 6):
            actual_count += mocked_output.count(f"\n{task_number}. ")

        # Assert
        expected_task_return = None
        expected_message = 5
        self.assertEqual(expected_task_return, actual_return)
        self.assertEqual(expected_message, actual_count)

    ### load_task()

    def test_load_task_empty_list_if_no_external_file_for_list(self):
        # Arrange
        file_name = "fake-test-task-list-.json"
        
        # Act
        task_manager = TaskManager(file_name)
        actual_action = task_manager.tasks

        # Assert
        expected_action = []
        self.assertEqual(expected_action, actual_action)

    def test_load_task_loads_correct_number_of_tasks_if_external_file_exists(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)

        # Act
        actual_tasks = len(task_manager.tasks)
        
        # Assert
        expected_tasks = 5
        self.assertEqual(expected_tasks, actual_tasks)

    def test_load_task_loads_correct_task_components_if_external_file_exists(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)

        # Act
        test_task = task_manager.tasks[0]
        actual_task_name = test_task.task_name
        actual_task_description = test_task.task_description
        actual_task_due_date = test_task.date_due
        actual_task_priority = test_task.priority
        actual_task_status = test_task.completed
        
        # Assert
        expected_task_name = "Test Task"
        expected_task_description = "Test task object"
        expected_task_due_date = "01-24-2026"
        expected_task_priority = "Low"
        expected_task_status = False
        self.assertEqual(expected_task_name, actual_task_name)
        self.assertEqual(expected_task_description, actual_task_description)
        self.assertEqual(expected_task_due_date, actual_task_due_date)
        self.assertEqual(expected_task_priority, actual_task_priority)
        self.assertEqual(expected_task_status, actual_task_status)

    ### save_task()

    def test_save_task_saves_empty_task_list_correctly(self):
        # Arrange
        task_manager = TaskManager(self.empty_task_list_save)

        # Act
        task_manager.save_task()
        actual_file = os.path.exists(self.empty_task_list_save)
        with open(self.empty_task_list_save, "r") as file:
            actual_contents = json.load(file)

        # Assert
        expected_contents = []
        self.assertEqual(expected_contents, actual_contents)
        self.assertTrue(actual_file)

    def test_save_task_saves_task_number_of_tasks_objects_correctly(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)

        # Act
        task_manager.filename = "test-task-list-saved.json"
        task_manager.save_task()
        actual_file = os.path.exists(task_manager.filename)
        with open(task_manager.filename, "r") as file:
            actual_contents = json.load(file)
        actual_number_of_tasks = len(actual_contents)

        # Assert
        expected_number_of_tasks = 5
        self.assertEqual(expected_number_of_tasks, actual_number_of_tasks)
        self.assertTrue(actual_file)

    def test_save_task_converts_objects_to_dict_correctly(self):
        # Arrange
        task_manager = TaskManager(self.test_task_list)

        # Act
        task_manager.filename = "test-task-list-saved.json"
        task_manager.save_task()
        with open(task_manager.filename, "r") as file:
            actual_contents = json.load(file)
        actual_task_name = actual_contents[3]["Name"]
        actual_task_description = actual_contents[3]["Description"]
        actual_task_date_due = actual_contents[3]["Due Date"]
        actual_task_priority_level = actual_contents[3]["Priority Level"]
        actual_task_status = actual_contents[3]["Status"]

        # Assert
        expected_task_name = "Trade"
        expected_task_description = "Crypto trade quota."
        expected_task_date_due = "12-30-2025"
        expected_task_priority_level = "High"
        expected_task_status = False
        self.assertEqual(expected_task_name, actual_task_name)
        self.assertEqual(expected_task_description, actual_task_description)
        self.assertEqual(expected_task_date_due, actual_task_date_due)
        self.assertEqual(expected_task_priority_level, actual_task_priority_level)
        self.assertEqual(expected_task_status, actual_task_status)

    ### add_task()
    def test_add_task_successfully_adds_task_object(self):
        # Arrange
        file_name = "add-task-test-list.json"
        if os.path.exists(file_name):
            os.remove(file_name)
        task_manager = TaskManager(file_name)


        # Act
        task_components = ["Test Task 1", "Test task to be added.", "08-30-2025", "Medium"]

        # Capturing the console printed message to keep test clean.
        with patch("builtins.input", side_effect=task_components), \
        patch("sys.stdout", new=StringIO()): 
            task_manager.add_task() 
        actual_tasks = task_manager.tasks
        actual_number_of_tasks = len(actual_tasks)

        # Assert
        expected_number_of_tasks = 1
        self.assertEqual(expected_number_of_tasks, actual_number_of_tasks)