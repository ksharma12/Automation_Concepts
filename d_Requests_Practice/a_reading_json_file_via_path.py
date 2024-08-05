import json

json_file = open('../d_Requests_Practice/Jsons/create_customer_copy.json', 'r')
json_data = json.load(json_file)
print(json_data["name"])