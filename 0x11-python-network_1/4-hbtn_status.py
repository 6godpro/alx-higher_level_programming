#!/usr/bin/python3
"""
    Fetches from a URL.
"""
import requests


if __name__ == "__main__":
    response = requests.get('https://alx-intranet.hbtn.io/status')
    response = response.content.decode('utf-8')
    print("Body response:")
    print(f"\t- type: {type(response)}")
    print(f"\t- content: {response}")
