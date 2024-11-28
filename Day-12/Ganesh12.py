'''AUTHOR:GANESH
28/11/24'''


first_set = set([12,13])
print("First set",first_set)

second_set = {78, 1000, 56, "Ganesh", 9.88}
print()
print("Second set",second_set)


r=second_set.add(11)
s=second_set.remove(9.88)
t=second_set.discard(56)
print("Added 11",r)
print()
print("Removed 9.88",s)
print()
print("Discarded 56",t)

another_set={78,88,90,5.87,2,334,85}

print("Union:", second_set |another_set)             
print("Intersection:", second_set & another_set)     
print("Difference (set1 - set2):", second_set - another_set)  
print("Symmetric Difference:", second_set ^ another_set)
