# Day 7: Looping through Lists

## Task
Practice using loops to iterate over items in a list.

## Description
Loops are useful for working with lists in Python, as they allow you to perform actions on each item in the list automatically. The `for` loop is commonly used to iterate over lists, making it easy to access each element in sequence.

## Key Concepts
- **For Loops**: Use `for` loops to go through each item in a list.
- **Range**: Use `range()` with loops to control the number of iterations.
- **Enumerate**: Use `enumerate()` to get both the index and the value of each item in the list.

## Example
```python
# Define a list of colors
colors = ["red", "blue", "green", "yellow"]

# Loop through each color and print it
for color in colors:
    print("Color:", color)
```

Output:
```plaintext
Color: red
Color: blue
Color: green
Color: yellow
```

Using enumerate:
```python
# Loop with index using enumerate
for index, color in enumerate(colors):
    print(f"Color at index {index} is {color}")
```

Output:
```plaintext
Color at index 0 is red
Color at index 1 is blue
Color at index 2 is green
Color at index 3 is yellow
```
