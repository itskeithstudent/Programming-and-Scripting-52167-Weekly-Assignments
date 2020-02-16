#A program that outputs whether or not today is a weekday.

#these two lists are lowercase, in case we get variance in use of case in user supplied string e.g. Monday/TUESdaY/etc.
weekdays = ("monday","tuesday","wednesday","thursday","friday")
weekend = ("saturday", "sunday")
#take in day of the week from user
curr_day=str(input("Enter what day of the week it is and I'll tell you whether it's the weekend or not. "))

if curr_day.lower() in weekdays:
    print("My sincere condolences, it is a week day, get back to work...")
elif curr_day.lower() in weekend:
    print("Congratulations it is the weekend, it will be a week day soon...")
else:
    print("Sorry you didn't enter a valid day")

#add logic to get current day from current date and time.
from datetime import datetime
todays_datetime = datetime.today()
today = todays_datetime.strftime('%A')
if today in weekdays:
    print("My sincere condolences, it is a week day, get back to work...")
else:
    print("Congratulations it is the weekend, it will be a week day soon...")