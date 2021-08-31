'''User inputs'''
print()
print('MEAL PRICE CALCULATOR')
print()
price_child = float(input("What is the price of a childs meal? : "))
price_adult = float(input("What is the price of an adult's meal? : "))
num_child = int(input("How many children are there? : "))
num_adult = int(input("How many adults are there? : "))
sales_tax_rate = int(input("What is the sales tax rate? : "))

'''Computation and print for subtotal'''
print()
subtotal = (num_child * price_child) + (num_adult * price_adult)
print(f"Subtotal: ${subtotal:.2f}")

'''Computation and print for sales tax'''
sales_tax_total = ((subtotal * sales_tax_rate) / 100)
print(f"Sales Tax: ${sales_tax_total:.2f}")

'''Computation and print for total'''
total = (subtotal + sales_tax_total)
print(f"Total: ${total:.2f}")
print()

'''Payment amount user input, and tip computation with returned change'''
payment_amount = float(input("What is the payment amount?: "))
tip_percent = float(input("What percent tip would you like to leave? (or 0 for none): "))
tip_num = ((total * tip_percent) / 100)
change = (payment_amount - total - tip_num)
print(f"Change: ${change:.2f}")
print()



