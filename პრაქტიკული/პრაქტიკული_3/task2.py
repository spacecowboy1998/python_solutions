import json

import requests

SERVICE_URL = "https://httpbin.org/post"
header = {"content-type": "application/json"}

about_car = {
    "brand": "Range Rover",
    "model": "2020 Land Rover Range Rover",
    "manufacturer": "Jaguar Land Rover",
    "price": 20000
}

response = requests.post(SERVICE_URL, data=json.dumps(about_car), headers=header)
if 200 <= response.status_code < 300:
    print("Car added successfully")
    print(f"status code: {response.status_code}")
else:
    print(f"Error occurred. Status code - {response.status_code}")
