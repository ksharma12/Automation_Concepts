import json
import requests

base_url = "https://api.stripe.com"  # base URL
auth_token = "Bearer 9e9772957078c06ddb151b154558a7efd6b4f57059d5896098daa4a6d30e5f7a"  # authentication
endpoint = "/public/v2/users"  # endpoint / path parameters

# get complete list of users of public of version v2
url = base_url + endpoint
headers = {"Authentication": auth_token}
response = requests.get(url=url, headers=headers)
