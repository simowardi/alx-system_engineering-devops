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
    # Check if the subreddit parameter is a string
    if not isinstance(subreddit, str):
        return 0

    # Prepare the URL for the Reddit API request
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    # Set a user-agent to avoid request blocking by Reddit
    headers = {"User-Agent": "Mozilla/5.0"}
    # Make the API request
    response = requests.get(api_url, headers=headers, allow_redirects=False)

    # If the request is successful, extract and return the subscriber count
    if response.status_code == 200:
        data = response.json()
        subscriber_count = data['data']['subscribers']
        return subscriber_count
    else:
        # Return 0 if the request was not successful
        return 0
