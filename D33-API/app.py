url = "http://api.open-notify.org/iss-now.json"
sun_url = "https://api.sunrise-sunset.org/json"
iss_response = {
    "timestamp": 1731568388,
    "message": "success",
    "iss_position": {"latitude": "-7.5287", "longitude": "123.4905"},
}

MY_LAT = 41.334095
MY_LONG = 69.221943
MY_ACC = ""
MY_PASS = ""
TO_ACC = ""
GMAIL_HOST = "smtp.gmail.com"
GMAIL_PORT = 587


import requests
from datetime import datetime
import smtplib
import time

parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}


def ISS():
    iss_response = requests.get(url)
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_latitude = float(iss_data['iss_position']['latitude'])
    iss_longitude = float(iss_data['iss_position']['longitude'])


    response = requests.get(sun_url, params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])

    time_now = datetime.utcnow()


    if time_now.hour >= sunset:
        if MY_LAT - 5 < iss_latitude < MY_LAT + 5 and MY_LONG - 5 < iss_longitude < MY_LONG + 5:
            with smtplib.SMTP(GMAIL_HOST, GMAIL_PORT) as connection:
                connection.starttls()
                connection.login(MY_ACC, MY_PASS)
                connection.sendmail(MY_ACC, TO_ACC, msg=f"Subject: ISS Position\n\n ISS is right above you")
    time.sleep(1)
    ISS()


ISS()