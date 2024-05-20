#!/usr/bin/python3
"""Python script to export data in the CSV format."""

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
    name = data[0].get('username')

    """#get info about tasks"""
    task_url = '{}/todos?userId={}'.format(my_api, user_id)

    response = requests.get(task_url)

    tasks = response.text
    """#parse data to json"""
    tasks = json.loads(tasks)

    completed = 0
    total_tasks = len(tasks)

    # csv
    mycsv = ""
    for task in tasks:
        mycsv += '"{}","{}","{}","{}"\n'.format(
            user_id,
            name,
            task['completed'],
            task['title']
        )
    with open('{}.csv'.format(user_id), 'w', encoding='UTF8') as csvFile:
        csvFile.write(mycsv)
