tuple1 = (1,2,3,4)
print(tuple1)           # Prints the Tuple

print(tuple1[0])        # Prints the first element

list1 = list(tuple1)    # Converts tuple to list

set1 = set(list1)       # Converts the list to a set

set1.add(5)             # Adds 5 as an element to the set

# set1 is {1,2,3,4,5} right now
set2 = {5,6,7,8,9,10}

# Prints the union of both sets. 
print(set1 | set2)      # You can also use set1.union(set2)

# Prints the intersection of both sets.
print(set1 & set2)     # You can also use set1.intersection(set2)

# Prints the difference of both sets. 
print(set1 - set2)      # You can also use set1.difference(set2)
