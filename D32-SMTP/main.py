import smtplib

my_user = "yodgorbeksheraliyev777@gmail.com"
password = "wefefwef"

connection  = smtplib.SMTP('smtp.gmail.com', port=587)
connection.starttls()
connection.login(user=my_user, password=password)
connection.sendmail(from_addr=my_user, to_addrs="eff", msg=f"Subject: Hello \n\n efwefwefwefew")
connection.close()
