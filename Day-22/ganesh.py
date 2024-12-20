og= {'name': 'Alice', 'age': 25, 'city': 'New York'}
print("original dictionary",og)
print("Keys:",og.keys())
print("Values:",og.values())

print("Key-Value Pairs:",og.items(),end=" ") 

print("Value for 'name':",og["name"])
print("Value for 'age':",og['age'])
print("Dictionary after pop:",og.popitem())
print("Dictionary after clear:",og.clear())
