#!/usr/bin/python3
"""Python script to export data in JSON format."""

import json
import requests

my_api = 'https://jsonplaceholder.typicode.com'


if __name__ == "__main__":

    # get users info
    users = '{}/users'.format(my_api)

    # get info
    response = requests.get(users)
    # pull data from api
    data = response.text
    """#parse data to json"""
    data = json.loads(data)

    # extract users data
    userData = {}
    for user in data:
        user_id = user.get('id')
        username = user.get('username')
        dict_key = str(user_id)
        userData[dict_key] = []
        # get user tasks
        tasks_url = '{}/todos?userId={}'.format(my_api, user_id)
        response = requests.get(tasks_url)

        # pull data
        tasks = response.text
        tasks = json.loads(tasks)

        for task in tasks:
            json_data = {
                "task": task['title'],
                "completed": task['completed'],
                "username": username
            }
            userData[dict_key].append(json_data)
    json_encode = json.dumps(userData)
    with open('todo_all_employees.json', 'w', encoding='UTF8') as userFile:
        userFile.write(json_encode)
