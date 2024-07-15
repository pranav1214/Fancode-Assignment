import requests

req_url = "http://jsonplaceholder.typicode.com"

def get_users():
    response = requests.get(f"{req_url}/users")
    response.raise_for_status()
    return response.json()

def get_todos():
    response = requests.get(f"{req_url}/todos")
    response.raise_for_status()
    return response.json()