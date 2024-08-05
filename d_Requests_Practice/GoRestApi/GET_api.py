import json
import requests

base_url = "https://gorest.co.in"  # base URL
auth_token = "Bearer 9e9772957078c06ddb151b154558a7efd6b4f57059d5896098daa4a6d30e5f7a"  # authentication
endpoint = "/public/v2/users"  # endpoint / path parameters

# get complete list of users of public of version v2
url = base_url + endpoint
headers = {"Authentication": auth_token}
response = requests.get(url=url, headers=headers)

print(f"response json is: {response.json()}")
print("---------------------------------------------------------------------------------------------")
print(f"response text is: {response.text}")
print("---------------------------------------------------------------------------------------------")
print(f"response status code is: {response.status_code}")
print("---------------------------------------------------------------------------------------------")
print(f"response request is: {response.request}")
print("---------------------------------------------------------------------------------------------")
print(f"response reason is: {response.reason}")
print("---------------------------------------------------------------------------------------------")
print(f"response headers is: {response.headers}")
print("---------------------------------------------------------------------------------------------")
print(f"response url is: {response.url}")
print("---------------------------------------------------------------------------------------------")
print(f"response content is: {response.content}")
print("---------------------------------------------------------------------------------------------")
print(f"response cookies is: {response.cookies}")
print("---------------------------------------------------------------------------------------------")
print(f"response elapsed is: {response.elapsed}")
print("---------------------------------------------------------------------------------------------")
print(f"response encoding is: {response.encoding}")
print("---------------------------------------------------------------------------------------------")
print(f"response history is: {response.history}")
print("---------------------------------------------------------------------------------------------")
print(f"response is redirect: {response.is_redirect}")
print("---------------------------------------------------------------------------------------------")
print(f"response is permanent redirect: {response.is_permanent_redirect}")
print("---------------------------------------------------------------------------------------------")
print(f"response raw is: {response.raw}")
print("---------------------------------------------------------------------------------------------")
print(f"response raise for status: {response.raise_for_status()}")
print("---------------------------------------------------------------------------------------------")
print(f"response apparent encoding is: {response.apparent_encoding}")
print("---------------------------------------------------------------------------------------------")
print(f"if 200 =< response < 400 than True else False: {response.ok}")
print("---------------------------------------------------------------------------------------------")
print(f"response is prepared request/None: {response.next}")
print("---------------------------------------------------------------------------------------------")
print(f"response is parsed header links of response: {response.links}")
print("---------------------------------------------------------------------------------------------")
print(f"response close is: {response.close()}")
print("---------------------------------------------------------------------------------------------")
print(f"request headers are: {response.request.headers}")
print("---------------------------------------------------------------------------------------------")
print(f"request url is: {response.request.url}")
print("---------------------------------------------------------------------------------------------")
print(f"request body is: {response.request.body}")
print("---------------------------------------------------------------------------------------------")
print(f"request method is: {response.request.method}")
print("---------------------------------------------------------------------------------------------")
print(f"request path url is: {response.request.path_url}")
print("---------------------------------------------------------------------------------------------")
print(f"request hooks is: {response.request.hooks}")

print("-------------------------------Json Library Methods--------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
print("-----------------------------------------------------------------------------------------------------")
# Json Library Methods ->
response_in_bytes = response.content
print(json.detect_encoding(response_in_bytes))
print("-----------------------------------------------------------------------------------------------------")
print(json.dumps(response.json(), indent=4))




