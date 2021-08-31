# Variables
print()
bank_accounts = []
bank_balances = []
new_account = ''
new_balance = 0

#Add items to each list
while new_account.lower() != 'quit':
    new_account = input('What is the name of this account? : ')

    if new_account.lower() != 'quit':
        new_balance = float(input('What is the balance of the account? : '))
        bank_accounts.append(new_account)
        bank_balances.append(new_balance)

#Prints lists
print()
print('Account Information:')
for i in range(len(bank_accounts)):
    print(f'{i + 1} {bank_accounts[i]} - ${bank_balances[i]:.2f}')

#Computation of total and average and print
print()
total = sum(bank_balances)
average = total / len(bank_balances)
max_bal = max(bank_balances)
max_index = bank_balances.index(max_bal)
print(f'Highest balance: {bank_accounts[max_index]} - ${bank_balances[max_index]:.2f}')
print(f'Total: ${total:.2f}')
print(f'Average: ${average:.2f}')
print()












