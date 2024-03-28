#!/usr/bin/python3
import requests
import json

letter = input("Enter a letter to search by (leave blank for all): ") or ""

data = {"q": letter}

response = requests.post("http://0.0.0.0:5000/search_user", json=data)

if response.status_code == 200:
  try:
    data = json.loads(response.text)

    if not data:
      print("No result")
    else:
      for user in data:
        print(f"[ {user['id']}] {user['name']}")
  except json.JSONDecodeError:
    print("Not a valid JSON")
else:
  print(f"Error: Server returned status code {response.status_code}")

