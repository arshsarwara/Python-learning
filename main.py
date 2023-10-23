'''API Request to Gitlab'''

#Python---->http request--->gitlab
#Python <----http response--gitlab

# We have a package in python; to make external request
# pip install requests ; Requests is http library
# we can also make request to change something on remote server

import requests

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
my_projects = response.json()

for project in my_projects:
    print(f"Project Name: {project['name']}\n Project Url: {project['web_url']}\n") # because the json is converted to dictionary as type

# print(response.text)
# print(type(response.text))   # string data type
#
# print(response.json()) #request json() function converts data from json into python data type
# print(type(response.json())) # becomes list data type
# print(response.json()[0])

