# Day 8: Using Loop Control Statements (break, continue, and pass)

## **Task**: Practice using `break`, `continue`, and `pass` in loops.

**Description**:
Control statements can manage loop flow:
- **`break`**: Exits the loop when a condition is met.
- **`continue`**: Skips the current iteration and moves to the next.
- **`pass`**: Does nothing; used as a placeholder.

**Example**:
```python
numbers = [1, 2, 3, 4, 5, 6]

# Using break
for num in numbers:
    if num == 4:
        break
    print(num)  # Output: 1, 2, 3

# Using continue
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)  # Output: 1, 3, 5

# Using pass
for num in numbers:
    if num == 3:
        pass
    print(num)  # Output: 1, 2, 3, 4, 5, 6
