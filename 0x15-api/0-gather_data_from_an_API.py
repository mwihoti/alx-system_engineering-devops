#!/usr/bin/python3
"""Script that returns information about employee"""
import json
import requests
import sys

my_api = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":

    user_id = sys.argv[1]
    user_info = '{}/users?id={}'.format(my_api, user_id)

    response = requests.get(user_info)
    data = response.text

    data = json.loads(data)
    name = data[0].get('name')

    """#get info about tasks"""
    task_url = '{}/todos?userId={}'.format(my_api, user_id)

    response = requests.get(task_url, user_id)

    tasks = response.text

    completed = 0
    total_tasks = len(tasks)
    """#parse data to json"""
    tasks = json.loads(tasks)

    """#get Task completed"""
    completed_tasks = []

    for task in tasks:
        if task.get('completed'):
            completed_tasks.append(task)
            completed += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(name, completed, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
