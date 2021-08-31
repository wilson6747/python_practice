#List creation
numbers = []
number_input = ''
print()
print('Enter a list of numbers, type 0 when finished.')

#Adding to the list
while number_input != 0:
    number_input = int(input('Enter Number: '))

    if number_input != 0:
        numbers.append(number_input)
print()

#Finds the sum
sum = 0
for number in numbers:
    sum += number
print(f'The sum is: {sum}')

#Finds the average
count = len(numbers)
average = sum / count
print(f'The average is: {average}')

#Finds the biggest number
biggest_num = 0
for number in numbers:
    if number > biggest_num:
        biggest_num = number
print(f'The largest number is: {biggest_num}')

#Finds the smallest positive number
smallest_num = 999999999
for number in numbers:
    if number > 0 and number < smallest_num:
        smallest_num = number
print(f'The smallest positive number is: {smallest_num}')

#Sorts list
sort_list = sorted(numbers)
print()
print('The sorted list is:')
for number in sort_list:
    print(number)


