#!/bin/bash
# Sends a POST request with email and subject variables to a URL
curl -s -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
