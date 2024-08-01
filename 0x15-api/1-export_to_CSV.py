#!/usr/bin/python3
import requests
import csv
import sys
"""Get employee data from API"""


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user_id = sys.argv[1]
    user_response = requests.get(url+'users/{}'.format(user_id))
    user = user_response.json()
    payload = {'userId': user_id}
    todo_response = requests.get(url+'todos', params=payload)
    todos = todo_response.json()
    with open(f'{user_id}.csv', 'w', newline='') as f_csv:
        writer = csv.writer(f_csv, quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([user_id,  user.get('username'), todo.get('completed'), todo.get('title')])
