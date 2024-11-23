'''
AUTHOR:INDHU SUBASH
DATE:23-11-24
'''
my_tuple = (10, 20, 80, 90,70)
print(my_tuple)
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])
list = list(my_tuple)
list.append(30)
my_tuple = tuple(list)
print("Tuple1"":", my_tuple)
my_set = {10, 50, 20, 80}
print("Set1:", my_set)
my_set.add(60)
my_set.remove(20)
print("Updated Set:", my_set)
set1 = {1, 2, 8, 4}
set2 = {3, 4, 5, 7}
print("Union:", set1.union(set2))