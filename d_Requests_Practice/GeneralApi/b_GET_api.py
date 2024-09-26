import requests

url = "https://reqres.in/api/users?page=2"

# response = requests.request(method="GET", url=url)
response = requests.request(url="https://reqres.in/api/users", method="GET", params="page=2")

print(response.text)
print(response.json())
