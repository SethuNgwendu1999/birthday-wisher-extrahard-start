import pandas as pd
import random
import smtplib
import datetime as dt

# Load birthday data from CSV
df = pd.read_csv("birthdays.csv")

# Remove a specific row from the DataFrame
df = df.drop(1)

# Define birthday data as a dictionary
birthdays = {
    'name': ["Sethu", "Benjamin", "Rele", "Ami", "Mother", "Neg"],
    'email': ["snupes@gmail.com", "Bejamin@gmail.com", "Rele@gmail.com", "Ami@gmail.com", "Mother@gmail.com", "sethun@gmail.com"],
    'year': [1999, 2001, 2007, 2015, 1983, 2015],
    'month': [8, 2, 4, 1, 4, 4],
    'day': [1, 3, 23, 9, 17, 29]
}

# Convert birthday dictionary to DataFrame
bf = pd.DataFrame(birthdays)

# Append new birthday data to the existing DataFrame
df = df._append(bf, ignore_index=True)

# Remove duplicate entries from the DataFrame
df = df.drop_duplicates()

# Save the updated DataFrame to a CSV file
df.to_csv('birthdays.csv', index=False)

# Get current date and time
now = dt.datetime.now()

# Extract day and month from the current date
current_day = float(now.day)
current_month = float(now.month)

# Extract birth month and day from the DataFrame
birth_month = df['month']
birth_day = df['day']

# Check if there are any birthdays today
if current_month in birth_month.values and current_day in birth_day.values:
    # Find rows with matching birth dates
    matching_rows = df[df['day'] == current_day]
    matching_name = matching_rows['name'].tolist()

    # Select a random letter template
    random_letter = random.randint(1, 3)
    with open(f'letter_templates\letter_{random_letter}.txt', 'r') as file:
        letter = file.read()
        letter = letter.replace('Dear [NAME],', f'Dear {matching_name[0]},')
        letter = letter.replace('Hey [NAME],', f'Hey {matching_name[0]},')
        print(letter)

    # SMTP Configuration
    my_email = "simplyxquisite01@gmail.com"
    password = "irtx ozqg itza zfbc"
    address_to = matching_rows['email'].tolist()

    # Send birthday email
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=address_to[0],
                            msg=f"Subject:Happy Birthday \n\n {letter}")
