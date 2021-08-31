#User input
print()
string_input = input('PLEASE TYPE SOMETHING: ')

#Function that recieves string and prints it out normally
def display_regular(string_input):
    print(string_input)

#Function that recieves string and prints it out in upper case
def display_uppercase(string_input):
    print(string_input.upper())

#Function that recieves string and prints it out in lower case
def display_lowercase(string_input):
    print(string_input.lower())

#Calls all the functions
display_regular(string_input)
display_uppercase(string_input)
display_lowercase(string_input)



