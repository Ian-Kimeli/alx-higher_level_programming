#!/usr/bin/python3
import requests

url = input("Enter the URL: ")
response = requests.get(url)

if response.status_code < 400:
  print(response.text)
else:
  print(f"Error code: {response.status_code}")
