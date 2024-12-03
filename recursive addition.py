"""
Name:Joe George
Title: Addition using recursion
Date: 3 December 2024
"""

def add_nums(a, b):
    if b == 0:
        return a
    else:
        return add_nums(a+1, b-1)

print(add_nums(10, 10))

