##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

user = "yodgorbeksheraliyev777@gmail.com"
password = "jjxy fiqd xyrj yrck"
import smtplib, random, pandas, datetime

today = datetime.datetime.now()
data = pandas.read_csv('./birthdays.csv')


for (index, row) in data.iterrows():
    if row['day'] == today.day and row['month'] == today.month:
        with open(f'./letter_templates/letter_{random.randint(1, 3)}.txt') as letter_file:
            wish = letter_file.read()
            wish = wish.replace('[NAME]', row["name"])
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user, password)
            connection.sendmail(from_addr=user, to_addrs=row['email'], msg=f"Subject: Happy Birthday \n\n {wish}")
    else: 
        continue

    # pass