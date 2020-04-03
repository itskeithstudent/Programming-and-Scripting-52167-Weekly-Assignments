#   Keith Ryan
#   Week 6 Assignment
#   function to get square root of user supplied number

#this function takes an original number and gets the square root of it
def sqrt(original_num):

    print(f"\nYou entered - {original_num}")
    #set square_root equal to half of the original number, this var will update as it is reassigned as part of calc. and will continue to do so till it is equal to temp
    square_root = original_num/2
    temp = 0
    #temp is reassigned once in the loop to be equal to square_root
    while (square_root!=temp):
        temp = square_root
        print(temp)
        #by repeatedly approximating a value we get closer and closer to the square root, we can say we have found the square root when the result
        #of the square_root calculation is the same as it was on the last loop
        #e.g. say we are getting square root of 9 but we've looped to point where when temp is 3 (meaning last loops square_root value was also 3)
        # ((9/3) + 3)/2 => 6/2 => 3
        square_root = ((original_num/temp) + temp)/2

    print(square_root)

#num takes a float value as the input
num = float(input("Enter a num to get square root of it: "))
sqrt(num)

#The above doesn't take too many loops to execute, please see below for some examples
'''
You entered - 9.0
4.5
3.25
3.0096153846153846
3.000015360039322
3.0000000000393214
3.0
3.0

You entered - 9.999
4.9995
3.49975
3.178405609329238
3.1621612670224426
3.1621195426076047
3.1621195423323263
3.1621195423323263

You entered - 100000000000.0
50000000000.0
25000000001.0
12500000002.5
6250000005.25
3125000010.625
1562500021.3125
781250042.6562495
390625085.32812124
195312670.66403267
97656591.33179264
48828807.664106764
24415427.817737076
12209761.79434379
6108975.981158149
3062672.6683637337
1547661.9443316166
806137.7689977181
465093.0222119024
340051.88661601284
317062.32795380044
316228.8643712705
316227.7660187454
316227.7660168379
316227.7660168379
'''
#could also do this as sqrt(int(input("Enter a num to get square root of it: "))), but I think this is less readable