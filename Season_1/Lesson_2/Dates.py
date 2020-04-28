# Functions to work with dates

# Import the datetime library to use dates
from datetime import datetime, timedelta

# Get the current date
current_date = datetime.now()

print("Today is the", str(current_date))

# Accessing single fields like days, month and year of the current date
print("Day:",str(current_date.day))
print("Month:",str(current_date.month))
print("Year:",str(current_date.year))

# timedelta is used to define a period of time
one_day = timedelta(days=1)
yesterday = current_date - one_day

print("Yesterday was the", str(yesterday))

one_week = timedelta(weeks=1)
last_week = current_date - one_week

print("Last week was the", str(last_week))

# Read a date from the command line and store it into a variable
birthday = input("When is your birthday (dd.mm.yyyy)? ")

birthday_date = datetime.strptime(birthday, '%d.%m.%Y')

print("Birthday:", str(birthday_date.date()))