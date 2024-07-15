def get_user_todos(todos, user_id):
    return [todo for todo in todos if todo["userId"] == user_id]

def todos_completed(todos):
    return [todo for todo in todos if todo["completed"]]

def get_percentage(todos):
    if not todos:
        return 0
    completed_todos = todos_completed(todos)
    return (len(completed_todos) / len(todos)) * 100