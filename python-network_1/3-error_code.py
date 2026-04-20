#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
Handles HTTP errors by catching urllib.error.HTTPError.
"""
import urllib.request
import urllib.error
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    req = urllib.request.Request(url, headers={'cf-clearance': 'true'})

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
