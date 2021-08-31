'''Input functions'''
print('Please answer the following questions to finish your ID card: ')
first_name = input("What is your first name? - ")
last_name = input('What is your last name? - ')
email_add = input('What is your email address? - ')
phone_num = input('What is your phone number? - ')
job_title = input('What is your job title? - ')
id_num = input('What is your ID number? - ')
hair_color = input('What is your hair color? - ')
eye_color = input('What is your eye color? - ')
month_start = input('What month did you start working at the company? - ')
training_adv = input('Have you completed advanced training? (Yes or No) - ')

'''title'''
print()
print('Listed below is your ID card:')
print()

'''name line'''
line1 = f'Name: {last_name}'
line1_2 = f'{first_name}'
print(line1.upper() + ', ' + line1_2.capitalize())

'''job title line'''
line2 = f'Title: {job_title}'
print(line2.capitalize())

'''ID number line'''
line3 = f'ID: {id_num}'
print(line3)

print()

'''Email address'''
line4 = f'Email: {email_add}'
print(line4.lower())

'''Phone number line'''
line5 = f'Phone: {phone_num}'
print(line5)

print()

'''hair color and eye color'''
line6 = f'Hair: {hair_color:<20}Eyes: {eye_color}'
print(line6)

'''Month and Training'''
line7 = f'Month: {month_start:<19}Training: {training_adv}'
print(line7)

print()