

my_list = [0,1,2,3,4,56,7,8,9,10]
print("Starting List")
print(my_list)

my_list.append(11)
print("\nAfter append(45):")
print(my_list)

my_list.extend([12,13])
print("\nAfter extend([55, 65]):")
print(my_list)

my_list.insert(14,15)
print("\nAfter insert(3, 30):")
print(my_list)

my_list.remove(0)
print("\nAfter remove(25):")
print(my_list)

removed_element = my_list.pop(4)
print("\nAfter pop(4):")
print(my_list)
print(f"(Removed element: {removed_element})")

index_of_35 = my_list.index(1)
print("\nIndex of 35:")
print(index_of_35)

count_of_15 = my_list.count(15)
print("\nCount of 15:")
print(count_of_15)

my_list.reverse()
print("\nAfter reverse():")
print(my_list)

my_list.sort()
print("\nAfter sort():")
print(my_list)

my_list.clear()
print("\nAfter clear():")
print(my_list)
