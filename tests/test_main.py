import pytest
from src.utils import user_fifty_per_todos

def test_assert_completed_percentage():
    result = user_fifty_per_todos()
    for res in result:
        assert res['complete_percentage'] > 50.0
    