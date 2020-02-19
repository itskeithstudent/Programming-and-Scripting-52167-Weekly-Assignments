#function to get square root of user supplied number

#this function takes an original number and gets the square root of it
def sqrt(original_num):

    print(f"\nYou entered - {original_num}")
    #set square_root equal to half of the original number, this var will update as it is reassigned as part of calc. and will continue to do so till it is equal to temp
    square_root = original_num/2
    temp = 0
    #temp is reassigned once in the loop to be equal to square_root
    while (square_root!=temp):
        temp = square_root
        #by repeatedly approximating a value we get closer and closer to the square root, we can say we have found the square root when the result
        #of the square_root calculation is the same as it was on the last loop
        #e.g. say we are getting square root of 9 but we've looped to point where when temp is 3 (meaning last loops square_root value was also 3)
        # ((9/3) + 3)/2 => 6/2 => 3
        square_root = ((original_num/temp) + temp)/2

    print(square_root)

num = int(input("Enter a num to get square root of it: "))
sqrt(num)