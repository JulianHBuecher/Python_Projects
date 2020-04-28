# Handling JSON data in Python

import json

# Create a dictionary object for conversion
person_dict = {"first":"Christopher","last":"Harrison"}
person_dict["City"] = "Seattle"
print(person_dict)

# Convert the dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)

# Create nested JSON Objects
# Create staff dictionary which assigns a person to a role
staff_dict = {}
staff_dict["Program Manager"]=person_dict

# Convert the dictionary to JSON object
staff_json = json.dumps(staff_dict)
print(staff_json)

# Create a list for the dictionary
# Create a list object of programming languages
languages_list = ["C#","Python","JavaScript"]

# Add list to dictionary
person_dict["languages"] = languages_list

# Convert dictionary to JSON object
person_json = json.dumps(person_dict)
print(person_json)