'''author:Ganesh
18/11/24
Loop control statements'''

numbers=[1,12,44,32,3,4,55,66]
for i in numbers:
    if i==55:
        break
    print(i,end=" ",)

print("                               ")

for j in numbers:
    if i%2==0:
        continue
    print(j,end=" ")
print("                                  ")
for k in numbers:
    if k*2==88:
        pass
    print(k,end=" ")
