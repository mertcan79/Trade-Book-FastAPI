import requests

# Set the endpoint URL and payload
url = "http://localhost:8000/trade"

payload_ABC = {"instrument_id": 'ABC', "traded_price": float(95), "quantity": 8, 'hedge': True}
payload2_ABC = {"instrument_id": 'ABC', "traded_price": float(100), "quantity": 7, 'hedge': True}
payload3_ABC = {"instrument_id": 'ABC', "traded_price": float(102), "quantity": 10, 'hedge': True}
payload4_ABC = {"instrument_id": 'ABC', "traded_price": float(90), "quantity": 5, 'hedge': True}
payload5_ABC = {"instrument_id": 'ABC', "traded_price": float(80), "quantity": 6, 'hedge': True}
payload6_ABC = {"instrument_id": 'ABC', "traded_price": float(87), "quantity": 7, 'hedge': True}
payload7_ABC = {"instrument_id": 'ABC', "traded_price": float(75), "quantity": 9, 'hedge': True}
payload8_ABC = {"instrument_id": 'ABC', "traded_price": float(101), "quantity": 12, 'hedge': True}
payload9_ABC = {"instrument_id": 'ABC', "traded_price": float(130), "quantity": 25, 'hedge': True}


payload_AAPL = {"instrument_id": 'AAPL', "traded_price": float(87), "quantity": 8, 'hedge': True}
payload2_AAPL = {"instrument_id": 'AAPL', "traded_price": float(109), "quantity": 7, 'hedge': True}
payload3_AAPL = {"instrument_id": 'AAPL', "traded_price": float(100), "quantity": 10, 'hedge': True}
payload4_AAPL = {"instrument_id": 'AAPL', "traded_price": float(90), "quantity": 5, 'hedge': True}
payload5_AAPL = {"instrument_id": 'AAPL', "traded_price": float(70), "quantity": 6, 'hedge': True}
payload6_AAPL = {"instrument_id": 'AAPL', "traded_price": float(67), "quantity": 7, 'hedge': True}
payload7_AAPL = {"instrument_id": 'AAPL', "traded_price": float(85), "quantity": 9, 'hedge': True}
payload8_AAPL = {"instrument_id": 'AAPL', "traded_price": float(106), "quantity": 12, 'hedge': True}
payload9_AAPL = {"instrument_id": 'AAPL', "traded_price": float(111), "quantity": 25, 'hedge': True}


payload_GOOG = {"instrument_id": 'GOOG', "traded_price": float(95), "quantity": 8, 'hedge': True}
payload2_GOOG = {"instrument_id": 'GOOG', "traded_price": float(102), "quantity": 7, 'hedge': True}
payload3_GOOG = {"instrument_id": 'GOOG', "traded_price": float(103), "quantity": 10, 'hedge': True}
payload4_GOOG = {"instrument_id": 'GOOG', "traded_price": float(92), "quantity": 5, 'hedge': True}
payload5_GOOG = {"instrument_id": 'GOOG', "traded_price": float(70), "quantity": 6, 'hedge': True}
payload6_GOOG = {"instrument_id": 'GOOG', "traded_price": float(97), "quantity": 7, 'hedge': True}
payload7_GOOG = {"instrument_id": 'GOOG', "traded_price": float(115), "quantity": 9, 'hedge': True}
payload8_GOOG = {"instrument_id": 'GOOG', "traded_price": float(103), "quantity": 12, 'hedge': True}
payload9_GOOG = {"instrument_id": 'GOOG', "traded_price": float(80), "quantity": 25, 'hedge': True}


# Make the POST request
response_ABC = requests.post(url, json=payload_ABC)
response2_ABC = requests.post(url, json=payload2_ABC)
response3_ABC = requests.post(url, json=payload3_ABC)
response4_ABC = requests.post(url, json=payload4_ABC)
response5_ABC = requests.post(url, json=payload5_ABC)
response6_ABC = requests.post(url, json=payload6_ABC)
response7_ABC = requests.post(url, json=payload7_ABC)
response8_ABC = requests.post(url, json=payload8_ABC)
response9_ABC = requests.post(url, json=payload9_ABC)

response_AAPL = requests.post(url, json=payload_AAPL)
response2_AAPL = requests.post(url, json=payload2_AAPL)
response3_AAPL = requests.post(url, json=payload3_AAPL)
response4_AAPL = requests.post(url, json=payload4_AAPL)
response5_AAPL = requests.post(url, json=payload5_AAPL)
response6_AAPL = requests.post(url, json=payload6_AAPL)
response7_AAPL = requests.post(url, json=payload7_AAPL)
response8_AAPL = requests.post(url, json=payload8_AAPL)
response9_AAPL = requests.post(url, json=payload9_AAPL)

response_GOOG = requests.post(url, json=payload_GOOG)
response2_GOOG = requests.post(url, json=payload2_GOOG)
response3_GOOG = requests.post(url, json=payload3_GOOG)
response4_GOOG = requests.post(url, json=payload4_GOOG)
response5_GOOG = requests.post(url, json=payload5_GOOG)
response6_GOOG = requests.post(url, json=payload6_GOOG)
response7_GOOG = requests.post(url, json=payload7_GOOG)
response8_GOOG = requests.post(url, json=payload8_GOOG)
response9_GOOG = requests.post(url, json=payload9_GOOG)
# Print the response
print(response9_ABC.text)
print(response9_AAPL.text)
print(response9_GOOG.text)
