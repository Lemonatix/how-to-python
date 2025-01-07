import requests

# URL of the REST API endpoint
a = 3
b = 6
url = f"http://localhost:1337/rechnung/{a}-sowie-{b}"

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    print("Response Data:", data)
else:
    print(f"Failed to fetch data. HTTP Status Code: {response.status_code}")