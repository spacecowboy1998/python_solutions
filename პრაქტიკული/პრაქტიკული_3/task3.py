import requests

SERVICE_URL = "https://httpbin.org/image/webp"

response = requests.get(f"{SERVICE_URL}")
if 200 <= response.status_code < 300:
    image = open("sample_image.png", "wb")
    image.write(response.content)
    image.close()
    print("Image has downloaded successfully")
    print(f"status code: {response.status_code}")
else:
    print(f"Error occurred. Status code - {response.status_code}")

