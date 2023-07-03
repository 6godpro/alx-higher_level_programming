#!/usr/bin/python3


import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/search/commits?q={query}{&page,per_page,sort,order}"
    response = requests.get('')
