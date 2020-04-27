# Code for Calling a API in the Azure Cloud Environment for Image Analyzation
# The Documentation for the API is here...
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Usage of requests library to simplify making a REST API call from Python
import requests  

# Usage of JSON library to read the data passed back by the webservice
import json

# Key to access the Computer Vision Service
import os
SUBSCRIPTION_KEY = os.getenv("AZURE_VISION_KEY")

# Address for the Computer Vision Service
vision_service_address = "https://julianspythonimageanalyzer.cognitiveservices.azure.com/"

# Name of the function to call to the address
address = vision_service_address + "vision/v2.0/analyze"

# Three optional parameters: language, details & visualFeatures for the analyze image function
parameters = {"visualFeatures":"Description,Color","language":"en"}

# Opening the image file tp get a file object containing the image to analyze
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, "rb").read()

# Specification of the subscription key and the content type in the HTTP header.
# Content-Type is application/octet-stream when passing an image
headers = {"Content-Type":"application/octet-stream",
            "Ocp-Apim-Subscription-Key":SUBSCRIPTION_KEY}

# For calling this function we have to use a HTTP POST
# response = request("post" ,address, headers=headers, params=parameters, data=image_data)
response = requests.post(address, headers=headers, params=parameters, data=image_data)

# Raise an exception if the call returns an error
response.raise_for_status()

# Display the JSON result returned
results = response.json()
print(json.dumps(results))

# Print the value for requestId from the JSON output
print()
print("requestId:\n"+results["requestId"])

# Print the dominantColorBackground from the color keys
print()
print("dominantColorBackground:\n"+results["color"]["dominantColorBackground"])

# Print the list of tags found in the description
print()
print("These are all the tags regarded to the picture: ")
for tags in results["description"]["tags"]:
    print(tags)

# Print the first tag in the description
print()
print("First tag in the description: "+results["description"]["tags"][0])