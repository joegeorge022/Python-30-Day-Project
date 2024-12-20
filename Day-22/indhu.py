og_list= {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("original dictionary",og_list)
print("Keys:",og_list.keys())
print("Values:",og_list.values())

print("Key-Value Pairs:",og_list.items(),end=" ") 

print("Value for 'name':",og_list["name"])
print("Value for 'age':",og_list['age'])
print("Dictionary after pop:",og_list.popitem())
print("Dictionary after clear:",og_list.clear())