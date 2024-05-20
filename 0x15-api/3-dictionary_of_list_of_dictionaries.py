#!/usr/bin/python3
"""
Display all employees' TODO list progress in JSON format.
Fetches details for all employees and their to-do list tasks from an API,
then exports the data to a JSON file.
"""

import json
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    file_name = 'todo_all_employees.json'
    users_resp = requests.get(f'{API_URL}/users/')
    users = users_resp.json()
    all_todos = {}

    for user in users:
        emp_id = user['id']
        todos_resp = requests.get(f'{API_URL}/todos?userId={emp_id}')
        todos = todos_resp.json()
        todos_list = []

        for todo in todos:
            task_info = {
                'username': user['username'],
                'task': todo['title'],
                'completed': todo['completed']
            }
            todos_list.append(task_info)
        
        all_todos[str(emp_id)] = todos_list

    with open(file_name, mode='w') as json_file:
        json.dump(all_todos, json_file)
