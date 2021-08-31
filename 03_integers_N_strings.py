'''User input - age'''
print()
age_num = int(input('What is your age? - '))

'''Add converted number variable to the number 1 then print to user'''
age_future = str(age_num + 1)
print('On your next birthday you will be ' + age_future + '!')

'''User input - egg cartons'''
print()
egg_num = int(input('How many egg cartons do you have? - '))

'''Multiply converted number variable by 12 and return to user'''
total_egg = str(egg_num * 12)
print('You have ' + total_egg + ' eggs!')

'''User input - cookies'''
print()
cookies_num = int(input('How many cookies do you have? - '))
people_num = int(input('How many people are there? - '))

'''Divide cookies by the amount of people and return to user'''
cookies_per_peep = str(cookies_num / people_num)
print('Each person may have ' + cookies_per_peep + ' Cookies!')
print()