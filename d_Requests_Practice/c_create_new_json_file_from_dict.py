# Data to be written
import json

dictionary = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phonenumber": "9976770500"
}

with open("../sample.json", "w") as outfile:
    json_data = json.dump(dictionary, outfile)
    print(json_data)
