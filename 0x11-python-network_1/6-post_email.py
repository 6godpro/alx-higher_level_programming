#!/usr/bin/python3
"""
    Sends a POST request to a URL with an email as data, and then
    displays the body of the response.

    USAGE: ./6-post_email.py <URL> <email>
"""
import requests
import sys


if __name__ == "__main__":
    url, email = sys.argv[1:]
    response = requests.post(url, {'email': email})
    print(response.content.decode('utf-8'))
