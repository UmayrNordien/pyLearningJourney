#write a program(function) that concatinates the letters ABCDEF and gives the sum of all numbers being 21

# a = 'ABC123DEF456'

# def answer(string):
#     alphabets = ''
#     result = 0
#     for char in string:
#         if char.isdigit():
#             result += int(char)
#         else:
#             alphabets += char
#     return (alphabets, result)
# print(answer(a))

x = 'zL2Aq3NrPbJm0i9BtV8yXl6Zx7YgHpKw1oRnQGcF5eWuOvMsTkUhIaD4fSjCvE'

def stringFormat(string):
    letters = []
    numbers = 0
    for char in string:
        if char.isdigit():
            numbers += int(char)
        else:
            letters += char
    return (letters, numbers)
print(stringFormat(x))



