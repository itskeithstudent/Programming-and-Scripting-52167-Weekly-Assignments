#   Keith Ryan
#   Week 2 Assignment
#Simple program to take user input for Weight (in kg) and Height (in cm)
#Then we caclulate the user height in meters squared, finally we calculate the BMI
user_weight_kg = int(input('Enter Weight (in Kg): ')) #Convert user input to int, assumes user will enter a int value
user_height_cm = int(input('Enter Height (in cm): '))
user_heigh_msquared = (user_height_cm/100)**2
user_bmi = round((user_weight_kg/user_heigh_msquared),2) #Round to two decimal palces the users bmi
print("BMI: ", str(user_bmi))
