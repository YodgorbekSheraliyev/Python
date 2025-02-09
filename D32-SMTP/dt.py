import datetime as dt
import smtplib
import random

account= ""
password = ""
host = "smtp.gmail.com"
to_account = "f"

current_time = dt.datetime.now()

with open('./quotes.txt', mode='r', encoding='utf-8') as file:
    quotes = file.readlines()

if current_time.weekday() == 1:
    quote = random.choice(quotes).strip()
    connection  = smtplib.SMTP(host=host, port=587)
    connection.starttls()
    connection.sendmail(from_addr=account, to_addrs=to_account, msg=f"Subject:Today's quote\n\n {quote}".encode('utf-8'))
    connection.close()