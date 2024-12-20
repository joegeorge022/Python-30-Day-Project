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

## 2. Nested Functions with Loops

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
