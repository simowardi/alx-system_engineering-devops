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

    user_agent = {'User-agent': 'Mozilla/5.0'}
    params = {'limit': 10}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)

    if response.status_code != 200:
        return None

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)
    all_data = response.json()

    try:
        raw1 = all_data.get('data').get('children')

        for i in raw1:
            print(i.get('data').get('title'))

    except:
        print("None")
