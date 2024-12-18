# Day 17: Exploring Functions and Recursion in Python

## **Task**: Understand and implement recursive functions while solidifying your understanding of functions.

**Description**:  
Recursion is a technique in which a function calls itself to solve a problem. Today’s task focuses on building a strong foundation in recursion by solving beginner-friendly problems and comparing recursive solutions with iterative ones.

In today’s task, you will:  
1. **Define recursive functions** to solve common problems.  
2. Compare recursion and iteration for problem-solving.  
3. Implement practical examples to understand recursion depth and base cases.

---

##  1. Factorial Using Recursion
Write a recursive function to calculate the factorial of a number.

```python
# Function to calculate factorial
def factorial(n):
    if n == 0 or n == 1:  # Base case
        return 1
    return n * factorial(n - 1)  # Recursive call

# Example usage
number = 5
print(f"Factorial of {number}: {factorial(number)}")  # Output: Factorial of 5: 120
```

---

##  2. Fibonacci Sequence Using Recursion
Create a recursive function to find the nth Fibonacci number.

```python
# Function to calculate Fibonacci number
def fibonacci(n):
    if n == 0:  # Base case
        return 0
    if n == 1:  # Base case
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive call

# Example usage
nth = 7
print(f"{nth}th Fibonacci number: {fibonacci(nth)}")  # Output: 7th Fibonacci number: 13
```

---

##  3. Sum of Digits Using Recursion
Define a recursive function to calculate the sum of the digits of a positive integer.

```python
# Function to calculate sum of digits
def sum_of_digits(n):
    if n == 0:  # Base case
        return 0
    return n % 10 + sum_of_digits(n // 10)  # Recursive call

# Example usage
number = 1234
print(f"Sum of digits of {number}: {sum_of_digits(number)}")  # Output: Sum of digits of 1234: 10
```

---

# YOU DONT HAVE TO DO THE 4TH EXERCISE. BUT IT IS NECESSARY THAT YOU UNDERSTAND IT.
##  4. Comparing Iterative and Recursive Solutions 
Solve the same problem (e.g., factorial) using iteration and recursion, then compare their outputs.

### Recursive Solution for Factorial
```python
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)
```

### Iterative Solution for Factorial
```python
def factorial_iterative(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage
number = 5
print(f"Recursive Factorial of {number}: {factorial_recursive(number)}")
print(f"Iterative Factorial of {number}: {factorial_iterative(number)}")
```

---

## Find Answers to the below Questions and tell Ganesh
1. What happens if a recursive function doesn’t have a base case?  
2. Compare the efficiency of recursion and iteration for calculating the Fibonacci sequence.  
3. Write a recursive function to reverse a string.
