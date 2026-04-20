#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the body of the response. If the status code is >= 400, prints an error.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url, headers={'cf-clearance': 'true'})
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
