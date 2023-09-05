# def reverse(string):
#     print(string[::-1])

# reversedString = reverse('Hello')
# print('data' , reversedString)  # no data is being returned

#solution:

def reverse(string):
    return(string[::-1]) #use return to return on variable, catches the data and stores in the variable
    print('test') #see the return doesnt return anything else but the stored variable
reversedString = reverse('Hello')
print('data', reversedString )
