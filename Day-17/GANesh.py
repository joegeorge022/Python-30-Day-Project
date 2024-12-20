def factorial(n):
    if n==1:
        return n
    else:
        return n * factorial(n-1)
n=int(input("Enter a Limit:"))
print(factorial(n))



def fibo(n):
    if n == 0: 
        return 0
    if n == 1: 
        return 1
    return fibo(n - 1) + fibo(n - 2)


n=int(input("Enter the limit:"))
print("Fibonacci number:",fibo(n))


def add(n1,n2):
    if n2==0:
        return n1
    else:
        return add(n1+1,n2-1)
n1=int(input("Enter number 1:"))
n2=int(input("Enter number 2:"))
print("Sum of",n1,"And",n2,"is",add(n1,n2))
