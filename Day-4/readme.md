# Day 4: Working with Strings in Python

### Ask for help if needed 🥹. Ganesh will help you✌️

## **Task**: Explore string manipulation and built-in string methods.

**Description**:
Strings are one of the most commonly used data types in Python. They allow you to store text data and perform various operations such as slicing, concatenation, and applying built-in methods. Today, you'll practice string operations and learn some of Python's powerful string methods to manipulate text efficiently.

## EVERYTHING IN THIS DAY'S TASK'S EXCEPT built-in methods like `lower()`, `upper()`, `split()`, and `replace()` HAVE BEEN DONE IN PYTHON LAB. SO THIS SHOULDN'T POSE A PROBLEM. 

**Key Concepts**:
- **String Declaration**: Declare strings using single or double quotes.
- **String Concatenation**: Combine strings using the `+` operator.
- **String Slicing**: Extract parts of a string using slicing notation.
- **String Methods**: Use built-in methods like `lower()`, `upper()`, `split()`, and `replace()` to modify strings.
- **Escaping Characters**: Handle special characters inside strings using backslashes (`\`).

**Example**:
```python
# Declaring strings
greeting = "Hello"
name = "Alice"

# String Concatenation
full_greeting = greeting + ", " + name + "!"
print(full_greeting)  # Output: Hello, Alice!

# String Slicing
message = "Welcome to Python"
print(message[0:7])  # Output: Welcome

# Using String Methods
sentence = "python is awesome"
print(sentence.lower())  # Output: python is awesome
print(sentence.upper())  # Output: PYTHON IS AWESOME
print(sentence.split())   # Output: ['python', 'is', 'awesome']
print(sentence.replace("awesome", "great"))  # Output: python is great

# Escape Characters
quote = "He said, \"Python is amazing!\""
print(quote)  # Output: He said, "Python is amazing!"
