#!/usr/bin/python3
"""This script fetches from a URL and displays some basic information about
the response.
"""
from urllib import request


if __name__ == "__main__":
    with request.urlopen('https://alx-intranet.hbtn.io/status') as request:
        response = request.read()
        print("Body response:")
        print("    - type:", type(response))
        print("    - content:", response)
        print("    - utf8 content:", response.decode('utf-8'))
