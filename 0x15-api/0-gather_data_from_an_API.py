#!/usr/bin/python3
import re
import sys
import requests
"""Get employee data from API"""


if __name__ == '__main__':
    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    response = requests.get(url + f'users/{user_id}').json()
    payload = {'userId': user_id}
    todo_response = requests.get(url + 'todos', params=payload)
    todos = todo_response.json()
    completed_tasks = []
    for todo in todos:
        if todo.get('completed') is True:
            completed_tasks.append(todo.get('title'))
    print(f'Employee {response.get("name")} is done with
          {len(completed_tasks)}/{len(todos)}: ')
    for completed_task in completed_tasks:
        print(f'\t {completed_task}')
