#!/usr/bin/python3
import urllib.request

url = input("Enter the URL: ")

try:
  with urllib.request.urlopen(url) as response:
    headers = response.headers

    request_id = headers.get('X-Request-Id')

    if request_id:
      print(f"X-Request-Id: {request_id}")
    else:
      print("X-Request-Id not found in response header.")
except urllib.error.URLError as e:
  print(f"Error: {e}")

