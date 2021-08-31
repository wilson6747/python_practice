# TITLE
print()
print('Welcome To The Shopping Cart Program! ')
print()

# Variables and Options list
shopping_cart_item = []
shopping_cart_price = []
choice = 0
while choice != 5:
    print('PLEASE SELECT ONE OF THE FOLLOWING :')
    print('1. Add Item')
    print('2. View Cart')
    print('3. Remove Item')
    print('4. Compute Total')
    print('5. Quit')
    choice = int(input('Please enter an action: '))
    print()

    # Add Item option
    if choice == 1:
        add_item = input('What item would you like to add? : ')
        price_item = float(input(f'What is the price of {add_item}? : '))
        shopping_cart_item.append(add_item)
        shopping_cart_price.append(price_item)
        print(f'[{add_item}] has been added to the cart.')
        print()

    # View Cart option 
    elif choice == 2:
        print('THE CONTENTS OF YOUR SHOPPING CART ARE : ')
        for i in range(len(shopping_cart_item)):
            print(f'{i + 1}. {shopping_cart_item[i]} - ${shopping_cart_price[i]:.2f}')
        print()

    # Remove item option
    elif choice == 3:
        print('THE CONTENTS OF YOUR SHOPPING CART ARE : ')
        for i in range(len(shopping_cart_item)):
            print(f'{i + 1}. {shopping_cart_item[i]} - ${shopping_cart_price[i]:.2f}')

        # Get input from user and delete item from both lists. If number is not in index, returns error.
        del_num = int(input('Which of the following item numbers would you like to delete? : ')) -1
        index_count = len(shopping_cart_item)
        if del_num > index_count and del_num > 0:
            print(f'There is no item [{del_num + 1}]')
        else:
            print(f'[{shopping_cart_item[del_num]}] removed from shopping cart. ')
            shopping_cart_item.pop(del_num)
            shopping_cart_price.pop(del_num)
        print()

    # Computes total and subtotal and returns it to the user
    elif choice == 4:
        print('BELOW IS THE TOTAL OF YOUR SHOPPING CART.')
        subtotal = sum(shopping_cart_price)
        print(f'Subtotal: ${subtotal:.2f}')
        total = subtotal * 1.0825
        print(f'Total: ${total:.2f}')
        print()

        #Club card computation and print
        club_card = input('Would you like to apply for a club card to save 20 percent off your order? [YES or NO] : ')
        if club_card.lower() == 'yes':
            club_total = total * .8
            print()
            print('BELOW IS YOUR CLUB DISCOUNTED TOTAL.')
            print(f'Club Total: ${club_total:.2f}')
            print()
        elif club_card.lower() == 'no':
            print('If you would like to later you can apply online at shop.com!')
            print()
        else:
            print('Incorrect input.')
            print('If you would like to later you can apply online at shop.com!')
            print()

    #Closes out loop or returns user to beggining of loop
    elif choice == 5:
        choice = 5

    else:
        print('PLEASE SELECT A NUMBER BETWEEN [1 - 5]')

print('THANK YOU FOR SHOPPING WITH US. HAVE A GREAT DAY!')
print()


    


