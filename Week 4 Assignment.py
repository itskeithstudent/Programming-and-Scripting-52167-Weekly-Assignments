#program takes integer input from user
user_input = int(input("Please enter a happy (positive) number - "))

#definition to do odd number calculation, when we get an odd number after dividing some number by 2
#we multiply it by three and add 1
def oddNum(odd_num):
    return (odd_num*3)+1

#if my user inputs 1 all we do is print 1
if(user_input==1):
    print(user_input)
#else we start to enter a while loop which remains true until the user_input is no longer > 1
else:
    while(user_input>=1):
        print(user_input)
        concat_operation = concat_operation + f' {user_input}'
        user_input = user_input//2
        if user_input % 2 and user_input != 1:
            print(user_input)
            concat_operation = concat_operation + f' {user_input}'
            user_input = oddNum(user_input)

print(concat_operation)



