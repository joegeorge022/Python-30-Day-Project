'''
AUTHOR:INDHU SUBASH
'''

set1={1,2,3,4,5,3,4}
set2={4,5,6,7,8,4,5}
print(f"union:{set1|set2}")
print(f"intersection:{set1&set2}")
print(f"difference:{set1-set2}")
print(f"symmetric difference:{set1^set2}")
set1.add(10)
set1.remove(1)
print(set1)