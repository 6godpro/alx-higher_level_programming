#!/usr/bin/python3
"""
    Sends a request to the URL and displays the body of the response.

    USAGE: ./3-error_code <URL>
"""
import sys
import urllib


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
