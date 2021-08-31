#Title
print()
print('PLEASE ENTER THE ITEMS OF THE SHOPPING LIST (TYPE QUIT TO FINISH)')

#Loop to store items in list
items_list = []
item_input = ''
while item_input.upper() != 'QUIT':
    item_input = input('Item: ')
    if item_input.upper() != 'QUIT':
        items_list.append(item_input)
print()

#Prints list without indexes
print('THE SHOPPING LIST IS: ')
for i in range(len(items_list)):
    print(f'{items_list[i]}')
print()

#Prints list with indexes
print('THE SHOPPING LIST WITH INDEXES IS: ')
for i in range(len(items_list)):
    print(f'{i + 1}. {items_list[i]}')
print()

#Deletes item and adds new item
change = int(input('Which item would you like to change? : ')) - 1
print(f'[{items_list[change]}] has been deleted from your list.')
items_list.pop(change)
new_item = input('What is the new item you would like to add? : ')
items_list.append(new_item)
print(f'[{new_item}] has been added to the list.')
print()

#Prints updated shopping list with indexes
print('THE UPDATED SHOPPING LIST WITH INDEXES IS: ')
for i in range(len(items_list)):
    print(f'{i + 1}. {items_list[i]}')
print()


