"""
Name:Joe George
Title: Factorial of a number (With & Without Recursion)
Date: 3 December 2024
"""

# 1. WITHOUT RECURSION
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

print(factorial(4))


# 2. WITH RECURSION
def recursion_factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(recursion_factorial(4))