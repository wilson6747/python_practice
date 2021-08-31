#List of people
print()
people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]
youngest_age = 9999
youngest_name = ''

#Splits list into two seperate lists for name and age
for line in people:
    seperate = line.split()
    name = seperate[0]
    age = int(seperate[1])
    print(f'NAME: {seperate[0]}, AGE: {seperate[1]}')

    #Find age that is youngest and name associated
    if age < youngest_age:
        youngest_age = age
        youngest_name = name
    print()
    print(f'The youngest person is: {youngest_name}, who is {youngest_age} years old.')

print()