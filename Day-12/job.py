"""
Author=Job thomas cherian
Date=25/11/24
"""
set1={1,3,2,4,3,4,5}
set2={4,5,6,7,8,3,7}
b=2
print(f"union {set1|set2}")
print(f"intersection:{set1&set2}")
print(f"difference: {set1-set2}")
set1.add(10)
set1.remove(3)
print(set1)
print(10 in set1)