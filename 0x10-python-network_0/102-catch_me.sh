#!/bin/bash
# Sends a request to a server and causes the server to respond with a message 'You got me!'.
curl -sL -X PUT -d "user_id=98" -H "Origin: School" "$1"
