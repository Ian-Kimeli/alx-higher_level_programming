#!/usr/bin/python3
import requests

url = input("Enter the URL: ")

response = requests.get(url)

if response.status_code == 200:
  request_id = response.headers.get("X-Request-Id")

  if request_id:
    print(f"X-Request-Id: {request_id}")
  else:
    print("X-Request-Id not found in response header.")
else:
  print(f"Error: Server returned status code {response.status_code}")

