import requests
import csv

def fetch_and_print_posts():
    """
    Fetches all posts from JSONPlaceholder and prints the titles.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post.get("title"))

def fetch_and_save_posts():
    """
    Fetches all posts and saves specific fields (id, title, body) into a CSV file.
    """
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        data_to_save = [
            {'id': post['id'], 'title': post['title'], 'body': post['body']}
            for post in posts
        ]

        fieldnames = ['id', 'title', 'body']

        with open('posts.csv', mode='w', encoding='utf-8', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
