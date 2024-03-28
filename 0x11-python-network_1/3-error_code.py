#!/usr/bin/python3
import urllib.request
import urllib.error

url = input("Enter the URL: ")

try:
  with urllib.request.urlopen(url) as response:
    data = response.read().decode("utf-8")
    print(data)
except urllib.error.HTTPError as e:
  print(f"Error code: {e.code} - {e.reason}")
except urllib.error.URLError as e:
  print(f"Error: {e}")

