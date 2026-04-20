#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    req = urllib.request.Request(url, headers={'cf-clearance': 'true'})

    with urllib.request.urlopen(req) as response:
        content = response.read()
        utf8_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(utf8_content))
