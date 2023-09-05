#Iterative recursion
def interativeFactorial(n):
    result = 1
    for i in range(n,0,-1):
        result = result * 1
    return result

print(interativeFactorial(5))

#Factorial recursion
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))