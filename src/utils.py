from src.resource_api import get_users, get_todos
from src.get_users import filter_users
from src.get_todos import get_user_todos, get_percentage


def user_fifty_per_todos():
    users = get_users()
    todos = get_todos()

    fancode_users = filter_users(users)

    assert fancode_users, "No user found in city"
    users_completed = []
    for user in fancode_users:
        user_todos = get_user_todos(todos, user["id"])
        complete_percentage = get_percentage(user_todos)

        if complete_percentage > 50:
            completed_users = {
                'user': user['id'],
                'username': user['name'],
                'complete_percentage': complete_percentage
            }
            users_completed.append(completed_users)
            print((f"User: {user['id']} - {user['name']} has completed task percentage: {complete_percentage}%"))
        else:
            print(
                f"User: {user['id']} - {user['name']} has completed task percentage less than or equal to 50%: {complete_percentage}%")

    return users_completed
