"""
AUTHOR : JOE MARTIN RINCE
DATE : 24-11-2024
"""

limit=int(input("Enter your limit: "))
i=0
L=[]
while i < limit:
    ty = input("Enter data type (S for String / N for Number): ").upper()

    if ty == "S":
        element = input("Enter the string element: ")
        L.append(element)
        i += 1
    elif ty == "N":
        try:
            element = int(input("Enter the number element: "))
            L.append(element)
            i += 1
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid type! Please enter 'S' or 'N'.")

print("Final list ",L,)