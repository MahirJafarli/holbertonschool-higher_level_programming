#!/usr/bin/python3
"""
A script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    q_letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': q_letter}
    url = 'http://0.0.0.0:5000/search_user'

    try:
        r = requests.post(url, data=payload, headers={'cf-clearance': 'true'})

        json_dict = r.json()

        if json_dict == {}:
            print("No result")
        else:
            user_id = json_dict.get('id')
            user_name = json_dict.get('name')
            print("[{}] {}".format(user_id, user_name))

    except ValueError:
        print("Not a valid JSON")
