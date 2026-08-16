# Day 23 - Fetching JSON data from a Web API

import json
import urllib.request

# Fetching sample data from a free public API
url = "https://jsonplaceholder.typicode.com/todos/1"

print("Sending request to API...")
response = urllib.request.urlopen(url)
data = response.read().decode("utf-8")

# Converting string response into a Python dictionary
json_data = json.loads(data)

print("API Response Received:")
print("User ID:", json_data["userId"])
print("Title:", json_data["title"])
print("Completed:", json_data["completed"])