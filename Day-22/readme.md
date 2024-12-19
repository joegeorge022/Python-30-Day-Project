# Day 22: Exploring Dictionary Operations

## **Task**: Implement and explore common dictionary-related functions and methods in Python.

**Description**:  
Dictionaries in Python are powerful data structures used to store key-value pairs. In today’s task, you will understand and demonstrate various dictionary operations such as retrieving keys, values, and items, and modifying or clearing a dictionary. These operations are crucial for managing and manipulating data efficiently.

---

### 1. Dictionary Keys and Values
Retrieve all the keys and values from a dictionary.

**Expected Output**:
```python
Original Dictionary: {'name': 'Alice', 'age': 25, 'city': 'New York'}
Keys: ['name', 'age', 'city']
Values: ['Alice', 25, 'New York']
```

### 2. Dictionary Items
Retrieve all key-value pairs from a dictionary.

**Expected Output**:
```python
Key-Value Pairs: [('name', 'Alice'), ('age', 25), ('city', 'New York')]
```

### 3. Accessing Values Using get()
Retrieve the value for a specific key.

**Expected Output**:
```python
Value for 'name': Alice
Value for 'age': 25
```

### 4. Updating the Dictionary
Update the dictionary with another dictionary.

**Expected Output**:
```python
Updated Dictionary: {'name': 'Alice', 'age': 26, 'city': 'New York', 'profession': 'Engineer'}
```

### 5. Removing a Specific Key-Value Pair Using pop()
Remove an entry using a key.

**Expected Output**:
```python
Removed Value for 'city': New York
Dictionary after pop: {'name': 'Alice', 'age': 26, 'profession': 'Engineer'}
```

### 6. Removing the Last Inserted Key-Value Pair Using popitem()
Remove the last key-value pair from the dictionary.

**Expected Output**:
```python
Removed Item: ('profession', 'Engineer')
Dictionary after popitem: {'name': 'Alice', 'age': 26}
```

### 7. Clearing the Dictionary
Remove all key-value pairs from the dictionary.

**Expected Output**:
```python
Dictionary after clear: {}
```

---

### Summary
Understanding and mastering these dictionary operations is essential for efficient data management in Python. These methods allow you to manipulate and process data with flexibility and precision. Experimenting with these examples will enhance your ability to handle real-world problems involving key-value data structures.

