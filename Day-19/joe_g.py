def fibonacci(n, a=0, b=1):
    if a > n:
        return
    print(a, end=" ")
    fibonacci(n, b, a + b)


print(fibonacci(25))
