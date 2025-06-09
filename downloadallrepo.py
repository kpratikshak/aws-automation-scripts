import requests
import os 

username = "your-username"
access_token = "your-access-token"

base_url = "https://api.github.com"

session = requests.Session()
session.auth =(username,access_token)

repositories_url = f"{base_url}/user/repos"
response = session.get(repositories_url)
repositories = response.json()

for repository in repositories:
    name = repository["name"]
    clone_url = repository["clone_url"]
    os.system(f"git clone {clone_url}")
    print(f"git clone {clone_url}")