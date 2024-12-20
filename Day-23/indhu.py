my_list = [10, 20, 30, 40]
print("Starting List")
print(my_list)



my_list.append(50)
print("\nAfter append(50):")
print(my_list)

my_list.extend([60, 70])
print("\nAfter extend([60, 70]):")
print(my_list)

my_list.insert(2, 25)
print("\nAfter insert(2, 25):")
print(my_list)

my_list.remove(30)
print("\nAfter remove(30):")
print(my_list)

removed_element = my_list.pop(3)
print("\nAfter pop(3):")
print(my_list)
print(f"(Removed element: {removed_element})")

index_of_50 = my_list.index(50)
print("\nIndex of 50:")
print(index_of_50)

count_of_20 = my_list.count(20)
print("\nCount of 20:")
print(count_of_20)

my_list.reverse()
print("\nAfter reverse():")
print(my_list)

my_list.sort()
print("\nAfter sort():")
print(my_list)

my_list.clear()
print("\nAfter clear():")
print(my_list)