#User input
print('Please input a rating from 1 to 10 to determine your')
print('eligibility for a loan.')
loan_size = int(input('How Large is the loan? : '))
credit = int(input('How good is your credit history? : '))
income = int(input('How high is your income? : '))
down_payment = int(input('How large is your down payment? : '))
should_loan = False

#If/Elif/Else
if loan_size >= 5:
    if credit >= 7 and income >= 7:
        should_loan = True
    elif credit >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False
    else:
        should_loan = False
else: # This means its a small loan
    if credit < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else:
            should_loan = False

#print statements
if should_loan:
    print('You qualify for a loan!')
else:
    print('You do not qualify for a loan.')
print()
