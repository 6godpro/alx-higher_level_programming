#!/bin/bash
# Sends a request to a server and causes the server to respond with a message 'You got me!'.
curl -sL -X PUT -H "Origin: School" -d "user_id=98" http://0.0.0.0:5000/catch_me_2
