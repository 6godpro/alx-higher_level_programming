#!/usr/bin/python3
"""
    Uses GitHub API along with GitHub credentials to retrieve user id.

    USAGE: ./10-my_github.py <username> <password>
"""
import requests
import sys


user, passwd = sys.argv[1:]
url = "https://api.github.com/user"
response = requests.get(url, auth=(user, passwd))
try:
    print(response.json().get('id'))
except Exception as e:
    pass
