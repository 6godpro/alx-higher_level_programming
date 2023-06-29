#!/bin/bash
# Displays the allowed HTTP methods on a server.
curl -sIX OPTIONS "$1" | grep Allow: | cut -b 8-
