grid =[ 
    [1,2,3],
    [4,5,6],
    [7,8,9],]
for row in grid:
    for element in row: 
        print(element,end=",")
    print()  
    
'''n=int(input("enter a number"))
for i range(1,n+1):
    for j in range(i):
        print("*",end="")
        print()'''
     
for i in range(1, 5):
    for j in range(1, 6+1):
        print(f"{i * j:3}", end=" ")
    print() 