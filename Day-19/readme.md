# Day 19: Fibonacci Sequence with Recursion

## **Task**: Use functions and recursion to print the Fibonacci sequence up to a number `N`.

**Description**:  
Recursion is a fundamental programming concept where a function calls itself to solve smaller instances of a problem. Today’s task focuses on printing the Fibonacci sequence using recursion. This exercise will help you deepen your understanding of recursion and function calls.

You will:  
1. Define a recursive function to generate the Fibonacci sequence.  
2. Pass parameters to control the current and next numbers in the sequence.  
3. Print all Fibonacci numbers less than or equal to a given number `N`.

---

## 1. Understanding Fibonacci Numbers
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting from 0 and 1.  
**Example**: 0, 1, 1, 2, 3, 5, 8, 13, 21...

---

## 2. Implementing the Recursive Function
Here is the Python code for the task:

```python
# Function to print Fibonacci sequence up to a number N
def print_fibonacci(n, a=0, b=1):
    if a > n:  # Base condition: stop if current number exceeds N
        return
    print(a, end=" ")  # Print the current number
    print_fibonacci(n, b, a + b)  # Recursive call with updated values

# Example usage:
n = 50
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
```

---

## 3. Step-by-Step Explanation
1. **Base Case**: The recursion stops when the current number `a` exceeds `N`.
2. **Recursive Call**: The function calls itself with `b` as the new current number and `a + b` as the new next number.
3. **Print Statement**: Each number in the sequence is printed during the recursive call.

---

## 4. Testing the Code
Run the code with different values of `N` to test its functionality. Examples:

### Input 1
```python
n = 20
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
```
**Output**:
```
Fibonacci numbers up to 20: 0 1 1 2 3 5 8 13 
```

### Input 2
```python
n = 100
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
```
**Output**:
```
Fibonacci numbers up to 100: 0 1 1 2 3 5 8 13 21 34 55 89 
```

---

## Bonus: Adding User Input
Allow users to input the maximum number for the Fibonacci sequence.

```python
# Prompt user for input
n = int(input("Enter the maximum number for the Fibonacci sequence: "))
print(f"Fibonacci numbers up to {n}:")
print_fibonacci(n)
```

---

### Summary
This task introduces recursion by solving a classic problem: generating the Fibonacci sequence. Experiment with the function and try different values of `N` to reinforce your understanding of recursion and function calls.
