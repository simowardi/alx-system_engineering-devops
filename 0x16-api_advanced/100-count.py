#!/usr/bin/python3
"""
Script that recursively counts occurrences of given keywords in hot articles
from a Reddit subreddit.
"""
import requests


def count_words(subreddit, word_list, after=None, counts={}):
    """
    Recursive function that queries the Reddit API, parses the titles of all
    hot articles, and prints a sorted count of given keywords.

    Args:
    subreddit (str): The subreddit to query.
    word_list (list): A list of keywords to count occurrences of.
    after (str): The 'after' parameter for pagination in Reddit API.
    counts (dict): Dictionary to store counts of keywords.

    Returns:
    None: If subreddit or word_list is empty or invalid.
    """
    if not word_list or word_list == [] or not subreddit:
        return

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}

    params = {"limit": 100}
    if after:
        params["after"] = after

    # Make a GET request to the Reddit API
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    # Check if the request was successful
    if response.status_code != 200:
        return

    # Parse the JSON response
    data = response.json()
    children = data["data"]["children"]

    # Iterate through each post's title
    for post in children:
        title = post["data"]["title"].lower()
        # Check each keyword in the word_list
        for word in word_list:
            # Count occurrences of the keyword in the lowercase title
            if word.lower() in title:
                counts[word.lower()] = counts.get(word.lower(), 0) + title.count(word.lower())

    # Get the 'after' parameter for pagination
    after = data["data"]["after"]
    if after:
        # Recursively call count_words with updated 'after' parameter
        count_words(subreddit, word_list, after, counts)
    else:
        # Sort counts by count value (descending) and word (ascending), then print
        sorted_counts = sorted(counts.items(),
                               key=lambda x: (-x[1], x[0].lower()))
        for word, count in sorted_counts:
            print(f"{word}: {count}")


if __name__ == '__main__':
    import sys
    # Check if subreddit and word_list are provided via command-line arguments
    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        # Extract subreddit and word_list from command-line arguments
        subreddit = sys.argv[1]
        word_list = sys.argv[2].split()
        # Call count_words function with subreddit and word_list
        count_words(subreddit, word_list)

