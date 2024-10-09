#!/usr/bin/python3
"""
This module will be used to contain functions which will
request something from an API and get its response
"""

import json
import requests
import csv


def fetch_and_print_posts():
    """
    Function which will fetch and print posts from a
    placeholder
    """

    URL = 'https://jsonplaceholder.typicode.com/posts'
    result = requests.get(URL)

    print("Status Code:{}".result.status_code)

    if result.status_code == 200:
        post = result.json()
        for post in posts:
            print("{}".post['title'])
    else:
        print("Failed to fetch posts")
fetch_and_print_posts()

def fetch_and_save_posts():
    """
    this function will be used to fetch and save posts from
    a placeholder
    """

    URL = 'https://jsonplaceholder.typicode.com/posts'
    result = requests.get(URL)

    print ("Status Code:{}".result.status_code)

    if result.status_code == 200:
        post = result.json()
        post_struct = []
        for posts in posts:
            post_struct: {
                    'id' = post['id'],
                    'title' = post['title'],
                    'body' = post['body'],
                }
            post_struct.append(post_struct)

        with open
