import math
def factorial(n):
    # Using built-in function available in Math module
    return(math.factorial(n))

n=int(input('enter number'))
f=factorial(n)
print("Factorial is : ",f)