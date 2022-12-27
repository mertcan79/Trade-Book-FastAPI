import requests

# Set the endpoint URL and payload
url = "http://localhost:8000/trade"
payload = {"instrument_id": 'ABC', "traded_price": float(95), "quantity": 10, 'hedge': True}

# Make the POST request
response = requests.post(url, json=payload)

# Print the response
print(response.text)
