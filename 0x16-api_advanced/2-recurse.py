#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a list containing
titles of all hot articles for a given subreddit.
"""


import requests


def recurse(subreddit, hot_list=[]):
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': 'custom'}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        res = res.json()
        for post in res.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if res.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
