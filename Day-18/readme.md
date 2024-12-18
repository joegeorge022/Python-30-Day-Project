# Day 18: Mastering Nested Loops in Python

## **Task**: Understand and apply nested loops to solve problems that involve multi-level iteration.

**Description**:  
Nested loops are loops within loops. They are often used to work with multidimensional data structures or to perform repeated operations at different levels. Today’s task will cover:

1. **Using nested loops** to iterate through lists and strings.
2. **Building patterns** using nested loops.
3. **Solving beginner-friendly exercises** to solidify the concept.

---

## 1. Using Nested Loops to Iterate Through a List of Lists

```python
# Define a 2D list (list of lists)
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Nested loop to print each element
for row in grid:
    for element in row:
        print(element, end=" ")
    print()  # Newline after each row
```
**Explanation**: The outer loop iterates over rows, while the inner loop iterates over elements within each row.

---

## 2. Building Patterns Using Nested Loops

```python
# Print a right-angled triangle pattern
n = 5  # Number of rows

for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()  # Newline after each row
```
**Output**:
```
*
**
***
****
*****
```
**Explanation**: The outer loop determines the row number, and the inner loop prints the stars for that row.

---

## 3. Creating a Multiplication Table

```python
# Multiplication table up to 5x5
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()  # Newline after each row
```
**Output**:
```
 1  2  3  4  5
 2  4  6  8 10
 3  6  9 12 15
 4  8 12 16 20
 5 10 15 20 25
```
**Explanation**: The outer loop controls the first multiplier, and the inner loop controls the second multiplier.

---

**Key Takeaways**:
- Nested loops are powerful for working with multidimensional data or solving multi-layered problems.
- Practice is essential to mastering nested loops, especially understanding how the inner and outer loops interact.

Complete these exercises to get hands-on experience with nested loops!
