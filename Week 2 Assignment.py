#Simple program to take user input for Weight (in kg) and Height (in cm)
#Then we caclulate the user height in meters squared, finally we calculate the BMI
user_weight_kg = int(input('Enter Weight: '))
user_height_cm = int(input('Enter Height: '))
user_heigh_msquared = (user_height_cm/100)**2
user_bmi = round((user_weight_kg/user_heigh_msquared),2)
print("BMI: ", str(user_bmi))
