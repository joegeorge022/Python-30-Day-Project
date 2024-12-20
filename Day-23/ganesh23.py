l=[10,20,30,40]
print()
print("After append(50):",l.append(50))
print()

print("After extend([60, 70]):",l.extend([60,70]))
print()
print("After insert(2, 25):",l.insert(2,25))
print()
print("After remove(30):",l.remove(30))
print()
print("After pop(3):",l.pop(3))
print()

print("Index of 50:",l.index(50))
print()

print("Count of 20:",l.count(20))

print()
m=l.sort()
print("After sort():",m)
print()
print("After reverse():",l[-1::-1])
print()
print("After clear():",l.clear())
print()


