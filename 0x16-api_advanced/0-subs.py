#!/usr/bin/python3
"""
Script to get the number of subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    If the subreddit is invalid, returns 0.
    """
    
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            data = response.json()
            subscriber_count = data['data']['subscribers']
            return subscriber_count
        except (ValueError, KeyError):
            return 0
    else:
        return 0
