'''AUTHOR:GANESH
13/11/24
List Functions'''

limit=int(input("Enter length of list:"))
i=0
L=[]
while i<limit:
    ty=input("enter data type: S/N :")
    if ty=="S":
        ele=input("enter the string element: ")
        L.append(ele)
        i+=1
    elif ty=="N":
        elem=int(input("enter the number element:"))
        L.append(elem)
        i+=1
    else:
        print("wrong code")
        break
print(L)
print("Number of elements",len(L))

s=["apple","orange"]
print(s)
s.remove("orange")
print("After removing orange",s)

        
