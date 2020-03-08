#   Keith Ryan
#   Week 5 Assignment
#   A program that outputs whether or not today is a weekday.
#   Original Solution takes input from the user
#   Best Solution takes todays date using datetime.datetime function
#   Alternate Solution takes similar approach to Best Solution but uses a dictionary key pairing to return the message

from datetime import datetime

#########################
### Original solution ###
#########################
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

#####################
### Best solution ###
#####################
#add logic to get current day from current date and time.
todays_datetime = datetime.today() #get todays date and time from calling datetimes today function
today = todays_datetime.strftime('%A') #get today using strftime function of datetime.datetime object
if str.lower(today) in weekdays: #same logic as above, but we don't need a final else block in case user enters wrong date as we don't have any user entry for here
    print("My sincere condolences, it is a week day, get back to work...")
else:
    print("Congratulations it is the weekend, it will be a week day soon...")

##########################
### Alternate solution ###
##########################
#Neat way of doing it with dictionary
#probably too much typing though, but is very readable
congrats_str = "Congratulations it is the weekend, it will be a week day soon..."
condolences_str = "My sincere condolences, it is a week day, get back to work..."
days_of_the_week_dict = {
    "Monday":condolences_str,
    "Tuesday":condolences_str,
    "Wednesday":condolences_str,
    "Thursday":condolences_str,
    "Friday":condolences_str,
    "Saturday":congrats_str,
    "Sunday":congrats_str
}

print(days_of_the_week_dict[today])
