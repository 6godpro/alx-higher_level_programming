#!/usr/bin/python3
"""
    Retrieve 10 commits from a repository sorted from recent to oldest.
"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/search/commits"
    user, repo = sys.argv[1:]
    url += f"?q=repo:{user}/{repo}&per_page=10&sort=committer-date"
    response = requests.get(url)
    try:
        for item in (response.json().get('items')):
            print("{}: {}".format(
                item['sha'],
                item['commit']['author']['name'])
                  )
    except KeyError:
        pass
