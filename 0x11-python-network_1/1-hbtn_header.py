#!/usr/bin/python3
"""
    Receives and sends a request to the provided URL and displays the
   value of the X-Request-Id header.
"""
from urllib import request
from sys import argv


if __name__ == "__main__":
    with request.urlopen(argv[1]) as response:
        print(response.headers.get('X-Request-Id'))
