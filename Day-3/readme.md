# Day 3: User Inputs

## **Task**: Use the input function to get user input in Python.

**Description**:
In Python, the `input()` function allows you to take input from the user. The input is read as a string, and you can convert it to other data types (e.g., int, float) if needed.

**Example**:
```python
# Get user input
name = input("Enter your name: ")
age = input("Enter your age: ")

# Convert age to an integer
age = int(age)

# Print the user input
print("Hello, " + name + "! You are " + str(age) + " years old.")
