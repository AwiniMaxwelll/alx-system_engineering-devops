#!/usr/bin/python3
import requests
import csv
import sys
"""Get employee data from API"""


if __name__ == "__main__":
     # Base URL for the JSONPlaceholder API
    url = 'https://jsonplaceholder.typicode.com/'
    # Get the employee information using the provided employee ID
    user_id = sys.argv[1]
    user_response = requests.get(url+'users/{}'.format(user_id))
    user = user_response.json()
     # Get the to-do list for the employee using the provided employee ID
    payload = {'userId': user_id}
    todo_response = requests.get(url+'todos', params=payload)
    todos = todo_response.json()
    # Write each item's details (user ID, username, completion status,
    #   and title) as a row in the CSV file
    with open(f'{user_id}.csv', 'w', newline='') as f_csv:
        writer = csv.writer(f_csv, quoting=csv.QUOTE_ALL)
        [writer.writerow([user_id,  user.get('username'), todo.get('completed'), todo.get('title')]) for todo in todos]
