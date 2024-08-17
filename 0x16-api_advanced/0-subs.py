#!/usr/bin/python3
"""Function that returns the number of subscribers of a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """returns the total number of subscribers of a given subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'linus:0x16.api.advanced:v1.0.0 (by /u/Lormax054)'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        result = response.json().get('data')
        return result.get('subscribers')
    else:
        return 0

