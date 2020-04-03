#   Keith Ryan
#   Week 4 Assignment
#   program takes integer input from user
#   It asks the user to input any positive integer and outputs the successive values of the following calculation.
#   At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. 
#   Have the program end if the current value is one.
user_input = int(input("Please enter a happy (positive) number - "))

#function to do odd number calculation, when we get an odd number after dividing some number by 2
#we multiply it by three and add 1
def oddNum(odd_num):
    return (odd_num*3)+1

concat_operation=user_input
#if my user inputs 1 all we do is print 1
if(user_input==1):
    print(user_input, end=' ')
#else we start to enter a while loop which remains true until the user_input is no longer > 1
else:
    #initialise concat_operation as blank
    #it gets all results of calculations appended to the end of it
    concat_operation=''
    #while user_input is still greater than or equal to one
    while(user_input>=1):
        #on first loop it will just use user_input as it was input, with a space to seperate it from next char
        concat_operation = concat_operation + f'{user_input} '
        user_input = user_input//2
        #if remainder after dividing user_input by two and user is not one then number is odd
        if user_input % 2 and user_input != 1:
            concat_operation = concat_operation + f'{user_input } '
            user_input = oddNum(user_input)
    #print concat_operation and strip whitespace from the end
    print(concat_operation.strip())





