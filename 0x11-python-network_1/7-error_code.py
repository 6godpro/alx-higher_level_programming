#!/usr/bin/python3
"""
    Displays the body of a response of a GET request.
    If the HTTP status code is greater than 400:
        * Display 'Error code: <status_code>'

    USAGE: ./7-error_code.py <URL>
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    if response.status_code < 400:
        print(response.content.decode('utf-8'))
    else:
        print(f"Error code: {response.status_code}")
