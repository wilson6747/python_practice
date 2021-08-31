'''user input for 2 integer numbers'''
print()
print('SIMPLE NUMBER COMPARING PROGRAM')
print('Please input 2 numbers to output a result')
print()
num_1 = int(input('What is the 1st number? : '))
num_2 = int(input('What is the 2nd number? : '))

'''Number comparing using if/else statemnts'''
if num_1 > num_2:
    print('The first number is greater')
else:
    print('The first number is not greater')
if num_1 == num_2:
    print('The numbers are equal')
else:
    print('The numbers are not equal')  
if num_2 > num_1:
    print('The second number is greater')
else:
    print('The second number is not greater')

'''User input for favorite animal then comparison using if/else statements'''
print()
fav_animal = input('What is your favorite animal? : ')
if fav_animal.lower() == 'dog':
    print('That is my favorite animal!')
elif fav_animal.lower() == 'cat':
    print('Ahh i see ... This is akward. I will see you later!')
else:
    print('That is not my favorite animal')
print()