#!/usr/bin/python3
"""
Script to recursively get the titles of all hot posts from a given subreddit.
"""

from requests import get


def recurse(subreddit, hot_list=[], after=None):
    """
    Function that queries the Reddit API and returns a list containing the
    titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The target subreddit.
        hot_list (list): List of titles of hot posts.
        after (str): The after parameter for pagination.

    Returns:
        list: List of titles of hot posts.
        None: If the subreddit is invalid.
    """
    if subreddit is None or not isinstance(subreddit, str):
        return None

    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    params = {'after': after, 'limit': 100}

    response = get(url, headers=user_agent, params=params,
                   allow_redirects=False)

    if response.status_code != 200:
        return None

    try:
        data = response.json().get('data', {})
        children = data.get('children', [])
        after = data.get('after')

        if not children:
            return hot_list if hot_list else None

        for child in children:
            hot_list.append(child.get('data', {}).get('title'))

        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    except (ValueError, KeyError):
        return None
