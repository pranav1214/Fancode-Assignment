import pytest
from src.utils import user_fifty_per_todos

def assert_completed_percentage(user):
    res = user_fifty_per_todos() 
    if res <= 50:
        message = (f"User {user['name']} (ID: {user['id']}) has not completed more than 50% "
                   f"of their todos (Completed {res:.2f}%)")
        raise AssertionError("User has not completed 50 percent of tasks")
    