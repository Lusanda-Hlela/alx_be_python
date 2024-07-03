# Explore 'datetime' Module

import datetime

from datetime import timedelta

def display_current_datetime():
    current_date = datetime.datetime.now()
    return current_date

# Displaying the current date and time
print(f"Current date and time: {display_current_datetime().strftime('%Y-%m-%d %H:%M:%S')}")

# Calculate a Future Date
def calculate_future_date():
  number_of_days = int(input("Enter the number of days to add to the current date: "))
  current_date = datetime.datetime.now()
  future_date = current_date + timedelta(days = number_of_days)
  return future_date.strftime('%Y-%m-%d')

print(f"Future date: {calculate_future_date()}")