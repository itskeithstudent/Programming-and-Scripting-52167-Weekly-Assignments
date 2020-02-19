#   Keith Ryan
#   Week 3 Assignment

#Take input from user as string, output every second letter in reverse order
user_input_str = str(input('Please enter a sentence: '))

#take first char off start of string
step_str = user_input_str[1:]
#now get every second char starting with the first char
step_str = step_str[::2]
#reverse the order of chars
reverse_step_str = step_str[::-1]
print(reverse_step_str)

#better solution
step_str = user_input_str[1::2]
reverse_step_str = step_str[::-1]
print(reverse_step_str)

#even better solution
step_str = user_input_str[1::2][::-1]
print(step_str)
