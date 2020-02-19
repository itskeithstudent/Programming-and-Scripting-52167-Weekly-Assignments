#   Keith Ryan
#   Week 5 Assignment
#   A program that outputs whether or not today is a weekday.

#these two lists are lowercase, in case we get variance in use of case in user supplied string e.g. Monday/TUESdaY/etc.
weekdays = ("monday","tuesday","wednesday","thursday","friday")
weekend = ("saturday", "sunday")
#take in day of the week from user
curr_day=str(input("Enter what day of the week it is and I'll tell you whether it's the weekend or not. "))

#if curr_day is in weekdays list then it is a week day, convert to lowercase incase their is variation in upper/lowercase
if curr_day.lower() in weekdays:
    print("My sincere condolences, it is a week day, get back to work...")
#if curr_day is in weekend list then it's a weekend, convert to lowercase incase their is variation in upper/lowercase
elif curr_day.lower() in weekend:
    print("Congratulations it is the weekend, it will be a week day soon...")
#else it's not a valid day
else:
    print("Sorry you didn't enter a valid day")

########################
###Alternate solution###
########################
#add logic to get current day from current date and time.
from datetime import datetime
todays_datetime = datetime.today() #get todays date and time from calling datetimes today function
today = todays_datetime.strftime('%A') #get today using strftime function of datetime.datetime object
if today in weekdays: #same logic as above, but we don't need a final else block in case user enters wrong date as we don't have any user entry for here
    print("My sincere condolences, it is a week day, get back to work...")
else:
    print("Congratulations it is the weekend, it will be a week day soon...")