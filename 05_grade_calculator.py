'''User input for grade percentage'''
print()
print('This program determines the letter grade you recieved based of the percent you recieved.')
grade_percent = int(input('What percent grade did you get? : '))

'''If/else/elif statements that set the variable of letter to the letter grade
and outputs to the user'''
print()
letter = ''
if grade_percent >= 90:
    letter = 'A'
elif grade_percent >= 80:
    letter = 'B'
elif grade_percent >= 70:
    letter = 'C'
elif grade_percent >= 60:
    letter = 'D'
else:
    letter = 'F'

'''calculates grade letter sign (+ or -)'''
sign = ''
last_digit = grade_percent % 10
if last_digit >= 7:
    sign = '+'
elif last_digit < 3:
    sign = '-'
else:
    sign = ''
if grade_percent >= 93:
    sign = ''
if letter == 'F':
    sign = ''

'''print'''
print(f'Your letter grade is: {letter}{sign}')

'''outputs wether or not you passed the class. 70 and up is passing'''
if grade_percent >= 70:
    print('You passed the class!')
else:
    print('You did not pass the class, keep trying!')
print()


