# QUESTION 1
list1 = [["Joe Martin", "Joe_George"], ["Job Thomas","Jon Bovi"]]

for guys in list1:
    for names in guys:
        print(names)
        
# QUESTION 2      
for i in range(6):
    for j in range(1,i+1):
        print(j,end="")
    print()
    
# QUESTION 3
for i in range(1, 11):
    print(f"Multiplication Table of {i} is : ")
    for j in range(1, 11):
        print(i*j)
    print()
