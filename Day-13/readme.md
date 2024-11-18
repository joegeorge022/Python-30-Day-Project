# Day 13: Introduction to Tuples

## **Task**: Learn to create, access, and use tuples in Python.

**Description**:  
Tuples are immutable data types in Python used to store ordered collections of items. They are defined using parentheses `()` and cannot be modified after creation.

### **Key Points**:
## Task 1: Create a Tuple

**Task**: Create a tuple with at least 5 elements of different data types.

**Instructions**:
1. Define a tuple containing elements of various data types, such as integers, floats, strings, and booleans.
2. Print the created tuple.

**Example**:
```python
# Example tuple
my_tuple = (1, "Python", 3.14, True, [1, 2, 3])
print(my_tuple)
 ```

## Task 2: Access Tuple Elements

**Task**: Print the 2nd and 4th elements of a tuple.

**Example**:
```python
my_tuple = (10, "Python", 3.14, "Hello", False)

# Access and print
print(my_tuple[1])  # Output: Python
print(my_tuple[3])  # Output: Hello
```

## Task 3: Unpack a Tuple

**Task**: Unpack a tuple into variables and print them.

**Example**:
```python
my_tuple = (1, "Code", 9.8)

# Unpack
a, b, c = my_tuple
print(a, b, c)  # Output: 1 Code 9.8
```

## Task 4: Modify a Tuple

**Task**: Try to change an element in a tuple and observe the error.

**Example**:
```python
my_tuple = (1, "Python", 3.14)

# Attempt to modify
my_tuple[0] = 10  # Error: 'tuple' object does not support item assignment
```
