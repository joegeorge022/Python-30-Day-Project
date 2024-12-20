"""
AUTHOR : JOE MARTIN RINCE
"""
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(6))

def fibonacci(m):
    if m==0:
        return 0
    elif m==1:
        return 1
    else:
        return fibonacci(m-1)+factorial(m-2)
print(fibonacci(5))

def sum_of_digits(l):

    if l < 10:
        return l
    else:

        return l % 10 + sum_of_digits(l// 10)


print("Sum of digits:", sum_of_digits(123456))
