# causing and handling errors and exceptions
# a = int(input())

#try...except
# try:
#     a = int(input('$'))
# except Exception:
#     print('User error')

#try...except as error (generic, will give the same error string for invalid inputs)
# try:
#     a = int(input('$ '))
# except Exception as error:
#     print('User error', 'error: ' + str(error))

# try:
#     a = int(input('~ '))
# except ValueError:
#     print('Invalid user input')
# except TypeError:
#     print('Type error')
# except KeyboardInterrupt:
#     print('Keyboard Interrupt')



#Practice
# Input addition +
# try: 
#     a = int(input('one: '))
#     b = int(input('two: '))
#     print(a + b)
# except ValueError:
#     print('Invalid error')

# Input division /
# try: 
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(int(x / y)) # in order to make it a whole number/Interger we put the division into a int() function to truncate the fractional part
# except ZeroDivisionError:
#     print('Value cannot be divided by 0')

# ^ improved example
try: 
    x = int(input('x: '))
    y = int(input('y: '))
    result = int(x /y)
    print(result)
except ZeroDivisionError:
    print('Value cannot be divided by 0')