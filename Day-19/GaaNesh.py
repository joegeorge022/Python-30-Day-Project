def print_fibonacci(n, first_num=0, second_num=1):
    if first_num > n: 
        return
    print(first_num, end=" ")  
    print_fibonacci(n, second_num, first_num + second_num)  

n =int(input("Enter a limit:"))
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
