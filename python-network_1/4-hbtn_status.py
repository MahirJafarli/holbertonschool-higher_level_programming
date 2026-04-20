#!/usr/bin/python3
"""
A script that fetches https://intranet.hbtn.io/status
using the requests package.
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    r = requests.get(url, headers={'cf-clearance': 'true'})
    
    content = r.text

    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
