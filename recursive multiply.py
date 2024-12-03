"""
Name:Joe George
Title: Multiplication using recursion
Date: 3 December 2024
"""

def multiply(a, b):
    if b == 1:
        return a
    else:
        return a + multiply(a, b-1)

print(multiply(10, 10))