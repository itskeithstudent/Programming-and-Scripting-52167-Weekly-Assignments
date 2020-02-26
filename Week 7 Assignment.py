#   Keith Ryan
#   Week 7 Assignment
# function to read in file and count number of letter 'e'
# Write a program that reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

# this function takes an input from user that should point to folder location containing a .txt file
def countLetterE(path):
    count=0
    textFile = open(path)
    textFileStr = textFile.read()
    for char in textFileStr:
        if char == 'e':
            count+=1
    print(count)

user_input = input("Enter the path to a file you want to count the times the letter e occurs: ")
countLetterE(user_input)