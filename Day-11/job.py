tuple = (10, 20, 30, 40, 50)
print("original tuple:", tuple)
print(f"first element:{tuple[0]}")
print(f"last element:{tuple[-1]}")
list = list(tuple)
list.append(60)
print(list)
set1={10,20,30,40,50}
set2={50,60,70,80}
print(f"original set{set1}")
"""set1.add(50)
set1.remove(20)"""
print(f"union:{set1.union(set2)}")
print(f"intersectiom:{set1.intersection(set2)}")
print(f"differenece:{set1.difference(set2)}")
