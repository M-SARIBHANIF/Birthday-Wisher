import datetime
import pandas
import random
import smtpd
my_email = "Enter Email"
my_password = "Enter Password"

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. e.g.
#name,email,year,month,day
#YourName,your_own@email.com,today_year,today_month,today_day
today = (datetime.datetime.now().month,datetime.datetime.now().day)
# HINT 2: Use pandas to read the birthdays.csv
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if (datetime.datetime.now().month, datetime.datetime.now().day) in birthdays_dict:
    birthday_person = birthdays_dict[datetime.datetime.now().month, datetime.datetime.now().day]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        content = letter_file.read()
        content = content.replace("[NAME]",birthday_person["name"])

    with smtpd.SMTP("smtp.gamil.com") as connection:
        connection.starttls()
        content.login(my_email,my_password)
        connection.sendmail(from_addr=my_email,to_addrs=birthday_person["email"],msg=f"Subject:Happy Birthday!\n\n{content}")


