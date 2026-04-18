#!/bin/bash
# Sends a JSON POST request with the contents of a file passed as the second argument.
curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1"
