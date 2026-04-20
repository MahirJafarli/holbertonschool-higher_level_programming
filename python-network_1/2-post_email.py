#!/usr/bin/python3
"""
A script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""
import urllib.parse
import urllib.request
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    values = {'email': email}
    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data=data, headers={'cf-clearance': 'true'})
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
