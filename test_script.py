import requests
response = requests.get("https://lau.edu.lb")

print(response.content)