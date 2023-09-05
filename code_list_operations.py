Characters = ['a', 'b', 'd', 'd', 'e']
print(Characters)

Characters[2] = 'c'  # Correcting the list by replacing value in list with a new one
print(Characters)

Characters.remove('e')  # Remove 'e' from the list
print(Characters)  # Print the updated list after removal

Characters.append('f')
print(Characters) # Print the updated list after adding a value to the list

'z' in Characters # Checking for value in list (Boolean)
