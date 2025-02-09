import requests
from datetime import datetime

TOKEN = "abdepfj34edf0eoir5o)"
USERNAME = "yodgorbek0920"
GRAPH_ID = "graph19"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# respone = requests.post(url=pixela_endpoint, json=user_params)
# print(respone.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {"X-USER-TOKEN": TOKEN}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_config = {
    "date": today.strftime("%Y%m%d"), 
    "quantity": "5", 
    "optionalData": '{"key":"value"}'
    }

# response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

pixel_put_endpoint = f"{pixel_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime("%Y%m")}{today.day - 1}"
pixel_put_endpoint_body = {
    "quantity": "15.5",
    "optionalData": '{"Run":"5km"}'
}
response = requests.put(url=pixel_put_endpoint, json=pixel_put_endpoint, headers=headers)
print(response.text)

