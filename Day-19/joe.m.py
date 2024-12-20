"""
AUTHOR : JOE MARTIN RINCE
"""

def print_fibonacci(n, a=0, b=1):
    if a > n:
        return
    print(a, end=" ")
    print_fibonacci(n, b, a + b)


n = int(input("Enter the maximum number for the Fibonacci sequence: "))
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)