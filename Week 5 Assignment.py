#A program that outputs whether or not today is a weekday.

weekdays = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
weekend = ["Saturday", "Sunday"]
#take in day of the week from user
curr_day=str(input("Enter what day of the week it is and I'll tell you whether it's the weekend or not. "))

if curr_day in weekdays:
    print("My sincere condolences, it is a week day, get back to work...")
elif curr_day in weekend:
    print("Congratulations it is the weekend, it will be a week day soon...")
else:
    print("Sorry you didn't enter a valid day")