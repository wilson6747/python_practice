#Empty friend list that will be added to
friends = []

friend_input = ''

while friend_input != 'end':
    friend_input = input('Type the name of a friend : ')

    if friend_input != 'end':
        friends.append(friend_input)
        
print()
print('Your friends are: ')

for friend in friends:
    print(friend)