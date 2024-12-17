def factorial(n):
    if n==0 or n==1:
        return 1
    return n* factorial(n-1)
number=3
print(f"factorial of {number}:{factorial(number)}")



def fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)
number=6
print(f"fibinocci of {number}:{fibonacci(number)}")


def sum_of_digits(n):
    if n==0:
        return 0
    return n%10+ sum_of_digits(n//10)
number=1234
print(sum_of_digits(number))


def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
number=5
print(factorial_iterative(number))
