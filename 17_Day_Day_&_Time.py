# Day 17 - Working with dates and time

from datetime import datetime

# Getting today's date and time
now = datetime.now()
print("Current date and time:", now)

# Printing just the year, month, and day
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

# Formatting the date to look nice
friendly_date = now.strftime("%d/%m/%Y")
print("Today's date is:", friendly_date)