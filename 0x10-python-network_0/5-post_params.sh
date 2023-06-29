#!/bin/bash
# Displays the body of a POST request's response.
curl --request POST "$1" -d "email=test@gmail.com&subject=I will always be here for PLD"
