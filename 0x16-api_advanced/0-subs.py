#!/usr/bin/python3
"""
Queries reddit api
"""
import requests


def number_of_subscribers(subreddit):
    """
    Defines a function that queries the Reddit API and returns the number
    of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0.
    """
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(reddit_url, headers=headers,
                                allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        subs = data['data']['subscribers']
        return subs
    else:
            return 0
   