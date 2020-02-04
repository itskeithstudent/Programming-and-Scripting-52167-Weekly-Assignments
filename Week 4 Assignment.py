#program takes integer input from user
user_input = int(input("Please enter a happy (positive) number - "))

def oddNum(odd_num):
    return (odd_num*3)+1

#if my user inputs 1 all we do is print 1
if(user_input==1):
    print(1)
#else we start to enter a while loop which remains true until the user_input is no longer > 1
else:
    while(user_input>=1):
        print(user_input)
        user_input = user_input//2
        if user_input % 2 and user_input != 1:
            print(user_input)
            user_input = oddNum(user_input)





