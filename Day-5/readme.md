# Day 5: Functions and Modular Programming

## **Task**: Create and use functions to modularize code in Python.

## I dont know how functions work in Python So lets learn together. Ask Ganesh if you have any doubts I guess. 
## Or [Click here](https://www.w3schools.com/python/python_functions.asp)

**Description**:
Functions are an essential part of Python, allowing you to break down your code into reusable blocks. Using functions helps to keep your code clean, organized, and easier to manage. Functions can take inputs, process them, and return outputs. By modularizing your code, you can avoid repetition and improve maintainability.

**Key Concepts**:
- **Defining Functions**: Use the `def` keyword to define a function.
- **Calling Functions**: Execute a function by calling its name.
- **Parameters**: Pass data to functions using parameters.
- **Return Values**: Return results from functions for further use.
- **Scope**: Understand local and global variables.

**Example**:
```python
# Define a function to greet a user
def greet(name):
    return f"Hello, {name}!"

# Define a function to calculate the area of a rectangle
def area_of_rectangle(length, width):
    return length * width

# Call the functions
print(greet("Alice"))                             # Output: Hello, Alice!
print("Area of rectangle:", area_of_rectangle(5, 3))  # Output: Area of rectangle: 15

