'''AUTHOR:GANESH
13/11/24
Functions'''


def smallest(num1,num2):
    if num1>num2:
        print(num1,"is Greater")
    elif num2>num1:
        print(num2,"is Greater")
    else:
        print("Both numbers are equal")

num1=int(input("Enter a number:"))
num2=int(input("Enter a number:"))

smallest(num1,num2)
