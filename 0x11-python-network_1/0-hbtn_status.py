#!/usr/bin/python3
import urllib.request


with urllib.request.urlopen(url) as response:

  data = response.read().decode("utf-8")

print("\t-".join(data.splitlines()))

