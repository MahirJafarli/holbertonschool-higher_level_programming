#!/bin/bash
# Displays only the status code of a response to a URL passed as argument.
curl -s -L -o /dev/null -w "%{http_code}" "$1"
