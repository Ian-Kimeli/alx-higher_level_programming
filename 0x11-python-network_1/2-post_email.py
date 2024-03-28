#!/usr/bin/python3
import urllib.parse
import urllib.request

url = input("Enter the URL: ")
email = input("Enter the email: ")

data = urllib.parse.urlencode({'email': email})

req = urllib.request.Request(url, data=data.encode(), method='POST')

try:
  with urllib.request.urlopen(req) as response:
    data = response.read().decode("utf-8")
    print(data)
except urllib.error.URLError as e:
  print(f"Error: {e}")

