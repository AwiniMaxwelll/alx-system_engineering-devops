#!/usr/bin/python3
"""
Returns to-do list information for a given employee ID.

This script takes an employee ID as a command-line argument and fetches
the corresponding user information and to-do list from the JSONPlaceholder API.
It then prints the tasks completed by the employee.
"""

import sys
import requests
"""Get employee data from API"""


if __name__ == '__main__':
    # Get the employee information using the provided employee ID
    user_id = sys.argv[1]
    # Base URL for the JSONPlaceholder API
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url + f'users/{user_id}').json()
    # Get the to-do list for the employee using the provided employee ID
    payload = {'userId': user_id}
    todo_response = requests.get(url + 'todos', params=payload)
    todos = todo_response.json()
    completed_tasks = []
    for todo in todos:
        if todo.get('completed') is True:
            completed_tasks.append(todo.get('title'))
    user_name = f'Employee {response.get("name")}'
    print(f'{user_name} is done with {len(completed_tasks)}/{len(todos)}: ')
    for completed_task in completed_tasks:
        print(f'\t {completed_task}')
