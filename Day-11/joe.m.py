"""
AUTHOR : JOE MARTIN RINCE
DATE : 24-11-2024
"""

my_tuple = (10, 20, 30, 40)
print("Original Tuple:", my_tuple)  
print("First Element:", my_tuple[0])
print("Last Element:", my_tuple[-1])

my_list = list(my_tuple)
my_list.append(50)
my_tuple = tuple(my_list)
print("Modified Tuple:", my_tuple)
my_set = {10, 20, 30, 40}
print("Original Set:", my_set)
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))