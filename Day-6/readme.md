# Day 6: Working with Lists

## **Task**: Understand and manipulate lists in Python.

**Description**:
Lists are a versatile data structure in Python that allow you to store and manipulate an ordered collection of items. You can add, remove, and access items in a list, making them useful for a wide range of tasks. Lists are defined using square brackets `[]`, and items are separated by commas.

**Key Concepts**:
- **Creating Lists**: Define a list using square brackets.
- **Accessing Elements**: Use indices to access specific items in a list.
- **Adding Elements**: Use `append()` to add items at the end of the list.
- **Removing Elements**: Use `remove()` to delete items from the list.
- **List Length**: Use `len()` to find the number of items in a list.

**Example**:
```python
# Define a list of fruits
fruits = ["apple", "banana", "cherry"]

# Access and print the first item
print("First fruit:", fruits[0])  # Output: First fruit: apple

# Add a new fruit to the list
fruits.append("orange")
print("Fruits after adding orange:", fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Remove a fruit from the list
fruits.remove("banana")
print("Fruits after removing banana:", fruits)  # Output: ['apple', 'cherry', 'orange']

# Find the number of items in the list
print("Number of fruits:", len(fruits))  # Output: 3
