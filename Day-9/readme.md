# Day 9: Creating Custom Lists

## **Task**: Implement a Python program to create a list with user-specified elements and types.

**Description**:  
In this task, you will create a Python program that allows a user to build a custom list by specifying the number of elements and their types (strings or numbers). This program introduces concepts of user input handling, loops, and data type operations.

### **Key Steps**:
1. **User Input for List Length**:  
   The user specifies how many elements the list will have. Use the `int` function to ensure the input is a number.

2. **Loop for Adding Elements**:  
   Use a `while` loop to add the specified number of elements to the list.

3. **Type Selection**:  
   - If the user selects "S", they will input a string.  
   - If the user selects "N", they will input a number.  
   - Handle invalid inputs gracefully.

4. **Output the Final List**:  
   Once all elements are added, print the complete list.

---

**Example**:
```python
# User specifies the length of the list
limit = int(input("Enter length of list: "))

# Initialize the counter and the list
i = 0
L = []

# Loop to collect elements
while i < limit:
    ty = input("Enter data type (S for String / N for Number): ").upper()
    
    if ty == "S":
        element = input("Enter the string element: ")
        L.append(element)
        i += 1
    elif ty == "N":
        try:
            element = int(input("Enter the number element: "))
            L.append(element)
            i += 1
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid type! Please enter 'S' or 'N'.")
    
# Output the final list
print("Final List:", L)
```






# Day 9: Creating Custom Lists

## Overview
Learn how to create a Python program that allows users to build custom lists with different data types. This exercise covers user input handling, loops, and type operations.

## Learning Objectives
- Handle user input for list creation
- Implement type validation
- Work with dynamic lists
- Practice error handling

## Implementation Details

### 1. User Input for List Length
The program starts by getting the desired list length from the user:
```python
limit = int(input("Enter length of list: "))
```

### 2. List Initialization
```python
i = 0
L = []
```

### 3. Element Collection Loop
```python
while i < limit:
    ty = input("Enter data type (S for String / N for Number): ").upper()
    
    if ty == "S":
        element = input("Enter the string element: ")
        L.append(element)
        i += 1
    elif ty == "N":
        try:
            element = int(input("Enter the number element: "))
            L.append(element)
            i += 1
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid type! Please enter 'S' or 'N'.")
```

### 4. Result Display
```python
print("Final List:", L)
```

## Example Usage
```
Enter length of list: 3
Enter data type (S for String / N for Number): S
Enter the string element: Hello
Enter data type (S for String / N for Number): N
Enter the number element: 42
Enter data type (S for String / N for Number): S
Enter the string element: World
Final List: ['Hello', 42, 'World']
```

## Key Concepts
- Type conversion using `int()`
- Exception handling with `try`/`except`
- List manipulation with `append()`
- String methods like `upper()`

## Practice Exercises
1. Modify the program to accept floating-point numbers
2. Add validation for string inputs (e.g., minimum length)
3. Implement a feature to remove elements from the list
4. Add support for more data types (e.g., boolean, complex numbers)

---
