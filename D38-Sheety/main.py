GOOGLE_SHEET_API = (
    "https://api.sheety.co/4922792f092ceacaa9a2ac2e2b40ae76/flight/sheet1"
)

import requests

body = {
    "workout": {
        "Name":"Yodgorbek",
        "id": 3,
    }
}

response = requests.get(url=GOOGLE_SHEET_API)
print(response.text)
