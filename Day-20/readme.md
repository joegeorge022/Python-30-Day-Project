# Day 20: Exploring Nested Functions in Python

## **Task**: Understand and implement nested functions to perform structured tasks.

**Description**:  
Nested functions are functions defined within other functions. They allow encapsulation, improving code readability and providing closure properties. Today, you will learn:

1. How to define nested functions.  
2. Using nested functions to structure complex logic.  
3. Benefits of closures in nested functions.

---

## 1. Defining a Nested Function

```python
# Outer function
def greet(name):
    # Inner function
    def message():
        return "Welcome!"

    return f"Hello, {name}. {message()}"

print(greet("Alice"))  # Output: Hello, Alice. Welcome!
```

## 2. Practical Example: Calculator with Nested Functions

Create a calculator function with nested functions for basic arithmetic operations.

```python
def calculator(a, b):
    def add():
        return a + b

    def subtract():
        return a - b

    def multiply():
        return a * b

    def divide():
        return a / b if b != 0 else "Division by zero!"

    return {
        "add": add(),
        "subtract": subtract(),
        "multiply": multiply(),
        "divide": divide()
    }

results = calculator(10, 5)
print("Addition:", results["add"])        # Output: Addition: 15
print("Subtraction:", results["subtract"]) # Output: Subtraction: 5
print("Multiplication:", results["multiply"]) # Output: Multiplication: 50
print("Division:", results["divide"])      # Output: Division: 2.0
```

## 3. Using Closures for Data Encapsulation

Closures in Python allow inner functions to retain the state of variables from their enclosing scope.

```python
def power(exponent):
    def calculate(base):
        return base ** exponent

    return calculate

square = power(2)  # Closure with exponent set to 2
cube = power(3)    # Closure with exponent set to 3

print(square(4))  # Output: 16
print(cube(2))    # Output: 8
```

## 4. Nested Functions with Loops

Combine nested functions and loops to process lists dynamically.

```python
def process_numbers(numbers):
    def square(n):
        return n ** 2

    def cube(n):
        return n ** 3

    results = {"squares": [], "cubes": []}
    for num in numbers:
        results["squares"].append(square(num))
        results["cubes"].append(cube(num))

    return results

numbers = [1, 2, 3, 4]
processed = process_numbers(numbers)
print("Squares:", processed["squares"])  # Output: Squares: [1, 4, 9, 16]
print("Cubes:", processed["cubes"])      # Output: Cubes: [1, 8, 27, 64]
```

---

### Summary
Today’s task introduces the concept of nested functions, demonstrating their utility for encapsulation, closures, and structured logic. Nested functions are a powerful tool for creating modular and efficient Python programs.
