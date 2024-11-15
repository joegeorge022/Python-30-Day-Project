# Day 3: User Inputs
Learn how to interact with users through Python's input function.

## Task
Learn to use the `input()` function in Python to gather user input.

## Description
The `input()` function in Python is used to take input from the user. By default, the input is captured as a string. To use the input as another data type (e.g., `int` or `float`), you need to explicitly convert it using functions like `int()` or `float()`.

## Example
```python
# Basic input
name = input("Enter your name: ")
print(f"Hello, {name}!")

# Converting input to integer
age = int(input("Enter your age: "))
print(f"In 5 years, you'll be {age + 5} years old")
```

## Resources
Check out this [Python Input Guide](https://www.w3schools.com/python/python_user_input.asp) for more examples and detailed explanations.

## Practice
Try creating programs that:
1. Ask for user's name and greet them
2. Get two numbers and perform calculations
3. Create a simple question-answer interaction
