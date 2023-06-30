#!/bin/bash
# Displays the response of a body.
curl -sX POST "$1" -H "Content-Type: application/json" -d "{}"
