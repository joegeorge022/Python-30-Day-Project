def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
    
print(factorial(4))


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

def sum(n):
    if n == 0:
        return 0
    return n % 10 + sum(n // 10)\

print(sum(123456789)) 
