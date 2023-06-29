#!/bin/bash
# Displays the body a response.
curl "$1" -o c.txt -sL && cat < c.txt  && rm c.txt
