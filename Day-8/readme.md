# Day 8: Loop Control Statements
Master the use of `break`, `continue`, and `pass` in Python loops.

## Task
Practice using loop control statements to manage program flow.

## Description
Python provides three key loop control statements:

1. **`break`**
   - Exits the loop immediately
   - Used when a certain condition is met

2. **`continue`**
   - Skips the current iteration
   - Continues with the next loop iteration

3. **`pass`**
   - Acts as a placeholder
   - Does nothing when executed

## Examples

### Using break
```python
numbers = [1, 2, 3, 4, 5, 6]
for num in numbers:
    if num == 4:
        break
    print(num)
```
Output:
```plaintext
1
2
3
```

### Using continue
```python
for num in numbers:
    if num % 2 == 0:
        continue
    print(num)
```
Output:
```plaintext
1
3
5
```

### Using pass
```python
for num in numbers:
    if num == 3:
        pass
    print(num)
```
Output:
```plaintext
1
2
3
4
5
6
```
