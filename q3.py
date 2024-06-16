#Write a python program that calculates the factorial of a given number.
'''a=int(input("enter the number"))
import math
print(math.factorial(a))'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * (n-1)

num = int(input("Enter a number: "))

if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = factorial(num)
    print(f"The factorial of {num} is {result}")
