my_set = {1,1,2,3,4,5,5}
print(my_set)  

my_set.add(30)
print("After adding 30:", my_set)

my_set.remove(5)
print("After removing 5:", my_set)

my_set.discard(40)
print("After discarding 40:", my_set)

print(10 in my_set)



set_a = {5, 10, 15}
set_b = {15, 20, 25}

union = set_a | set_b
print("Union:", union)  

intersection = set_a & set_b
print("Intersection:", intersection)  

difference = set_a - set_b
print("Difference:", difference)  

symmetric_diff = set_a ^ set_b
print("Symmetric Difference:", symmetric_diff)
