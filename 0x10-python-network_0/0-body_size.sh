#!/bin/bash
# Sends a request to a given URL, and displays the size of the response body.
curl "$1" -o size.txt -s ; cat < size.txt | wc -c ; rm -f size.txt
