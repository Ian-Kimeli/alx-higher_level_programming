#!/usr/bin/python3
import requests

url = "https://alx-intranet.hbtn.io/status"

response = requests.get(url)
if response.status_code == 200:
 data = response.text

 print("\t-".join(data.splitlines()))
else:
 print(f"Error: Server returned status code {response.status_code}")

