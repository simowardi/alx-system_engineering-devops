#!/usr/bin/python3
"""
Export employee to-do list data in CSV format.
Fetches employee details and to-do list tasks from an API and exports to CSV.
"""

import csv
import requests
import sys

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    emp_id = sys.argv[1]
    file_name = f'{emp_id}.csv'
    emp_resp = requests.get(f'{API_URL}/users/{emp_id}')
    emp_data = emp_resp.json()
    todos_resp = requests.get(f'{API_URL}/todos?userId={emp_id}')
    todos = todos_resp.json()

    with open(file_name, mode="w") as file:
        writer = csv.writer(file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)
        for todo in todos:
            writer.writerow([todo['userId'], emp_data['username'],
                             todo['completed'], todo['title']])
