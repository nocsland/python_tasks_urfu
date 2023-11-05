import requests

response = requests.get("https://urfu.ru")
print(response.headers)
