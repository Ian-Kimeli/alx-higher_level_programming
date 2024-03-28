#!/usr/bin/python3
import requests
import sys

repository_name = sys.argv[1]
owner_name = sys.argv[2]

url = f"https://api.github.com/repos/{owner_name}/{repository_name}"

response = requests.get(url)

if response.status_code != 200:
    print("Error: Could not retrieve repository information.")
    if response.status_code == 404:
        print("Repository not found.")
    else:
        print(f"Unexpected response status code: {response.status_code}")
else:
    data = response.json()

    print("Repository Name:", data["name"])
    print("Owner Name:", data["owner"]["login"])
    print("Description:", data["description"])
    print("Created at:", data["created_at"])
    print("Stars:", data["stargazers_count"])
    print("URL:", data["html_url"])
