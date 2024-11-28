"""
AUTHOR : JOE MARTIN RINCE
DATE : 25-11-2024
"""

empty_set=set()
sample_set = {1,2,3,"hi",1.23}
duplicate_set={1,2,3,3,3,4,4}
print(duplicate_set)

sample_set.add(20)
sample_set.remove(3)
sample_set.discard(23)
print(sample_set)


set1={1,2,3,4,5}
set2={4,5,6,7,8,9}
print("union:",set1|set2)
print("intersection: ",set2&set1)
print("difference:",set1-set2)
print("symmetric",set1 ^ set2)