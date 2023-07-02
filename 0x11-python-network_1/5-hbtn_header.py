#!/usr/bin/python3
"""
    Sends a request to the provided URL and displays value of a
    header variable.
"""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
