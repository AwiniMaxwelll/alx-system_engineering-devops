#!/usr/bin/python3
import re
import sys
import requests
"""Get employee data from API"""

url = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if re.fullmatch(r'\d+', sys.argv[1]):
            request = requests.get('{}/users/{}'.format(url, id)).json()
            todos = requests.get('{}/todos'.format(url)).json()
            emp_name = request.get('name')
            tasks = list(filter(lambda x: x.get('userId') == id, todos))
            completed = list(filter(lambda x: x.get('completed'), tasks))
            print("Employee {} is done with tasks({}/{}):".format(
                emp_name,
                  len(completed), 
                  len(tasks)))
            if len(completed) > 0:
                for task in completed:
                    print("\t {}".format(tasks.get('title')))
