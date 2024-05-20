#!/usr/bin/python3
"""
Fetches and displays employee to-do list progress.
Given an employee ID, this script fetches the employee's details and their
to-do list tasks from a placeholder API and prints the completed tasks.
"""

import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    emp_id = sys.argv[1]
    emp_resp = requests.get(f'{API_URL}/users/{emp_id}')
    emp_data = emp_resp.json()
    todos_resp = requests.get(f'{API_URL}/todos?userId={emp_id}')
    todos = todos_resp.json()
    completed = [todo for todo in todos if todo['completed']]

    print(f"Employee {emp_data['name']} is done with tasks"
          f"({len(completed)}/{len(todos)}):")
    for todo in completed:
        print(f"\t {todo['title']}")
