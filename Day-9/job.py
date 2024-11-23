"""""
Authour:Job Thomas Cherian
Date: 16/11/24
"""
limit=int(input("Enter the limit:"))
i=0
L=[]
while i<limit:
    user_input=input("enter a data type(S for string/ N for number/F for floating numbers):").upper()
    if user_input=="S":
        element=input("Enter a string:")
        L.append(element)
        i+=1
    elif user_input=="N":
        try:
            element=int(input("enter a number:"))
            L.append(element)
            i+=1
        except ValueError:
            print("inavlid input .Try a number")
    elif user_input=="F":
        try:
          element=float(input("Enter a floating number:"))
          L.append(element)
          i+=1
        except ValueError:
            print("invalid input. Try a decimal number")
    else:
        print("wrong input.Please enter 'S' or 'N' or 'F'")

print("final list:",L)
sent=" ".join(map(str,L))
print(sent)


