'''AUTHOR:GANESH
28/11/24'''

#TUPLES

my_tuple=(12,2,45,76,54,78,98,76,9)
print("Original Tuple",my_tuple)
print( )
print("The First Element",my_tuple[0])
print( )
print("The Second Element",my_tuple[1])
print( )
print("The Third Element",my_tuple[2])
print( )
print("The Last Element",my_tuple[-1])
print( )


#CONVERTING TO LIST

my_list=list(my_tuple)
print("Original List",my_list)
print( )
my_list.append(87)
print("List after appending",my_list)
print( )
part=my_list[3:6]
print("A part of the list",part)
print( )

#COVERTING TO TUPLE

tup=tuple(my_list)
print("New tuple",tup)
print( )

#SETS

my_set={12,45,65,78,99,87,45,4,10}
print("Original Set",my_set)
print( )
my_set.add(98)
my_set.remove(99)
print("Set after adding and removing",my_set)
print( )
my_set.discard(12)
print("Set after discarding",my_set)
print( )

#SET FUNCTIONS
set1={12,4,2,3,67}
set2={22,5,7,99,67}

print("Union:", set1.union(set2))
print( )
print("Intersection:", set1.intersection(set2))
print( )
print("Difference:", set1.difference(set2))
print( )
