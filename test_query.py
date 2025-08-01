import requests
import json

# Define the API endpoint
url = "http://localhost:5000/query"

# Define the natural language query you want to test
payload = {
    "text": "total quantity by region"
}

# Set the headers to specify JSON
headers = {
    "Content-Type": "application/json"
}

try:
    # Send the POST request
    response = requests.post(url, headers=headers, data=json.dumps(payload))

    # Check for a successful response
    if response.status_code == 200:
        print("✅ Response received from API:")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"❌ Error {response.status_code}: {response.text}")

except Exception as e:
    print("❌ Exception occurred:", str(e))
