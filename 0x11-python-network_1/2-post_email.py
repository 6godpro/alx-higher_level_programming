#!/usr/bin/python3
"""
    Receives a URL and an email then send a POST request to the URL with
    the email as a parameter, finally displays the body of the response.
"""
from urllib import (
    parse,
    request.Response,
    request.urlopen
)
from sys import argv


if __name__ == "__main__":
    value = {'email': argv[2]}

    data = parse.urlencode(value)  # convert dict to URL string
    data = data.encode('ascii')  # convert to bytes
    req = request.Request(argv[1], data)
    with request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
