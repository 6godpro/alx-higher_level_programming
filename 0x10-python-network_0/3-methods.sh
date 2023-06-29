#!/bin/bash
# Displays the allowed HTTP methods on a server.
curl -sIX OPTIONS 0:5000/route_4 | grep Allow | cut -b 8-
