#!/usr/bin/python3
"""
Script to get the number of subscribers on a given Reddit subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.

    Args:
    subreddit (str): The subreddit name to query.

    Returns:
    int: The number of subscribers of the subreddit.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Mozilla/5.0"}

    # Make a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        # Return 0 if the subreddit is invalid or request fails
        return 0
