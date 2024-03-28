#!/usr/bin/python3
import requests

url = input("Enter the URL: ")
email = input("Enter the email address: ")

data = {"email": email}

response = requests.post(url, json=data)

if response.status_code == 200:
  print(response.text)
else:
  print(f"Error: Server returned status code {response.status_code}")
