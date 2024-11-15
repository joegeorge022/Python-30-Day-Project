# Day 1: Variables in Python
Learn the fundamentals of storing and managing data in Python.

## Task
Understand and use variables in Python programming.

## Description
A variable is a container for storing data values. In Python, variables:
- Don't need type declarations
- Can change types after being set
- Store different kinds of data

## Example
```python
# Declare variables
full_name = "Joe George"
age = "18"
is_student = True

# Print variable values
print(f"Hello {full_name}!")
print(f"Your name is {full_name} and you are {age} years old.")
print(f"Are you a student? Ans: {is_student}")

# Conditional printing
if is_student:
    print("He is a student")
else:
    print("He is not a student")
```

## Expected Output
```plaintext
Hello Joe George!
Your name is Joe George and you are 18 years old.
Are you a student? Ans: True
He is a student
```
