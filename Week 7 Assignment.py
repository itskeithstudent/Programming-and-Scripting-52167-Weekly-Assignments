#   Keith Ryan
#   Week 7 Assignment
# function to read in file and count number of letter 'e'
# Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

import sys
# this function takes an input from user that should point to folder location containing a .txt file
def countLetterE(path):
    count=0 #count is initialised to 0 on calling function as we have yet to count any 'e's
    textFile = open(path) #open user supplied path
    textFileStr = textFile.read() #take the file we've opened, read it and store in string variable textFileStr
    for char in textFileStr: #for each character in textFileStr check if 'e'
        if char.lower() == 'e': #consider case where e is upper or lower case
            count+=1
    print(count) #once we've parsed through every char in textFileStr print the count

#try except blocks first trys to get commandLineInput
try:
    commandLineInput = sys.argv[1]
    countLetterE(commandLineInput)
#if user hasn't entered filename in command line then prompt them to type a path
except:
    userInput = input("Enter the path to a file you want to count the times the letter e occurs: ")
    countLetterE(userInput)


