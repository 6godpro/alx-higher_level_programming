#!/usr/bin/python3
"""
    This script takes in a letter and sends a POST request to
    a URL.
    Display:
        * If the body is JSON formatted: [<id>] <name>
        * If the body is JSON formatted but empty: No result
        * Otherwise: NOt a valid JSON

    USAGE: ./8-json_api.py <letter>
"""
import requests
import sys


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    value = "" if len(sys.argv) == 1 else sys.argv[1]
    response = requests.post(url, data={'q': value})
    try:
        _dict = eval(response.content.decode('utf-8'))
        if type(_dict) is dict:
            if len(_dict) != 0:
                print(f"[{_dict['id']}] {_dict['name']}")
            else:
                print("No result")
    except Exception as e:
        print("Not a valid JSON")
