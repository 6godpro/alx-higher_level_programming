#!/bin/bash
# Displays the status code of the response.
curl -I -sw "%{http_code}" "$1"
