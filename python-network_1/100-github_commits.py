#!/usr/bin/python3
"""
Python script that takes 2 arguments (repo name and owner name)
and uses the GitHub API to list the 10 most recent commits.
"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"

    try:
        response = requests.get(url)
        commits = response.json()

        for i in range(min(10, len(commits))):
            sha = commits[i].get('sha')
            author_name = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author_name}")
            
    except Exception:
        pass
