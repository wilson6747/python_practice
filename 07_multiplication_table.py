#User input
print('MULTIPLICATION TABLE')
user_num = int(input('How many columns and rows do you want in your multiplication table? : '))
num_lines = user_num + 1

#Multiplication and output
for row_num in range(1, num_lines):
    for col_num in range(1, num_lines):
        mult_num = row_num * col_num
        print(f'{mult_num:3}', end = '')
    print()