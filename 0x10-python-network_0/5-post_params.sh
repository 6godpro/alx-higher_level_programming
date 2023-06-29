#!/bin/bash
# Displays the body of a POST request's response.
curl -X POST "$1" -sd "email=test@gmail.com&subject=I will always be here for PLD"
