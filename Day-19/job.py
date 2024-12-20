def print_fibonacci(n, a=0, b=1):
    if a>n:
        return
    print(a,end=" ")
    print(n,b,a+b)
n = 45
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
