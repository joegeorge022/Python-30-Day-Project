"""
AUTHOR : JOE MARTIN RINCE
"""



original_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}


keys = list(original_dict.keys())


values = list(original_dict.values())


print("Original Dictionary:", original_dict)
print("Keys:", keys)
print("Values:", values)

key_value_pairs = list(original_dict.items())

print("Key-Value Pairs:", key_value_pairs)




value_name = original_dict['name']
value_age = original_dict['age']

print("Value for 'name':", value_name)
print("Value for 'age':", value_age)


original_dict['age'] = 26
original_dict['profession'] = 'Engineer'


print("Updated Dictionary:", original_dict)



removed_value = original_dict.pop('city')


print("Removed Value for 'city':", removed_value)
print("Dictionary after pop:", original_dict)




removed_item = original_dict.popitem()


print("Removed Item:", removed_item)
print("Dictionary after popitem:", original_dict)

original_dict.clear()

print("Dictionary after clear:", original_dict)


