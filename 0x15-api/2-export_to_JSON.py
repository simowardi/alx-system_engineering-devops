#!/usr/bin/python3
"""
Display the employee TODO list progress in JSON format.
Fetches the employee's details and their to-do list tasks from an API,
then exports the data to a JSON file.
"""

import json
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    emp_id = sys.argv[1]
    file_name = f'{emp_id}.json'
    emp_resp = requests.get(f'{API_URL}/users/{emp_id}')
    emp_data = emp_resp.json()
    todos_resp = requests.get(f'{API_URL}/todos?userId={emp_id}')
    todos = todos_resp.json()

    all_tasks = {}
    user_todos = []
    for todo in todos:
        task_info = {
            'task': todo.get('title'),
            'completed': todo.get('completed'),
            'username': emp_data.get('username')
        }
        user_todos.append(task_info)

    all_tasks[str(emp_id)] = user_todos

    with open(file_name, mode="w") as json_file:
        json.dump(all_tasks, json_file)
