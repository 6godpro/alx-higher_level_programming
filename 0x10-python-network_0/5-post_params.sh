#!/bin/bash
# Displays the body of a POST request's response.
curl --request POST "$1" -sd "email=test@gmail.com&subject=I will always be here for PLD"
