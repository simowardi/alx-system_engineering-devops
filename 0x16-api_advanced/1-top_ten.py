#!/usr/bin/python3
"""
Script to get the titles of the first 10 hot posts from a given subreddit.
"""

from requests import get


def top_ten(subreddit):
    """
    Function that queries the Reddit API and prints the titles of the first
    10 hot posts listed for a given subreddit.

    Attributes:
        subreddit (str): The target subreddit.
    """
    if subreddit is None or not isinstance(subreddit, str):
        print(None)
        return

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    try:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post.get('data', {}).get('title'))
    except (ValueError, KeyError):
        print(None)

