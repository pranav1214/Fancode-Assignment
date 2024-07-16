import sys
import os
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))

from utils import user_fifty_per_todos

def assert_completed_percentage(user, completed_percentage):
    if completed_percentage <= 50:
        message = (f"User {user['name']} (ID: {user['id']}) has not completed more than 50% "
                   f"of their todos (Completed {completed_percentage:.2f}%)")
        raise AssertionError("Not completed 50 percent of tasks")