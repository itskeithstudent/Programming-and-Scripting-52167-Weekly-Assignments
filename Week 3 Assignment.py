#   Keith Ryan
#   Week 3 Assignment

#Take input from user as string, output every second letter in reverse order
print("I will print every second letter in reverse if you type in a sentence.") #Give some context before prompting user
user_input_str = str(input('Please enter a sentence: ')) #take in user input as str, will work even if we get a number

### Below have done this 3 different ways, reassign variables as we go, I felt like this should be possible with just one line ###
#take first char off start of string
step_str = user_input_str[1:]
#now get every second char starting with the first char
step_str = step_str[::2]
#reverse the order of chars
reverse_step_str = step_str[::-1]
print(reverse_step_str)

#better solution
step_str = user_input_str[1::2] #go from first character to last character in steps of 2
reverse_step_str = step_str[::-1] #reverse order of the str
print(reverse_step_str)

#even better solution
print(user_input_str[1::2][::-1]) #go from first character to last character in steps of 2 and reverse order of str and print to screen in one line
