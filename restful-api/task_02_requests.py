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

    print(f"Status Code: {result.status_code}")

    if result.status_code == 200:
        posts = result.json()
        for post in posts:
            print(f"{post['title']}")
    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    """
    this function will be used to fetch and save posts from
    a placeholder
    """

    URL = 'https://jsonplaceholder.typicode.com/posts'
    result = requests.get(URL)

    print(f"Status Code:{result.status_code}")

    if result.status_code == 200:
        posts = result.json()
        post_struct = []
        for post in posts:
            post_data = {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body'],
                }
            post_struct.append(post_data)

    with open('posts.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.DictWriter(file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(post_struct)
