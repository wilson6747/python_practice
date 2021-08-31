'''Take user input for farenheit and convert to celcius'''
print()
print('This program will convert Farenheit to Celcius for you automatically!')
print()
fahr_num = float(input('What is the temperature in Farenheit? : '))
cels_num = (fahr_num - 32) * 5 / 9
print(f'The temperature is {cels_num} degrees.')