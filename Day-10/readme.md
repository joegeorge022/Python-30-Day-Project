# Day 10: Working with Loops and Lists

## **Task**: Use loops to manipulate and iterate over a list of numbers.

**Description**:  
In this task, you will practice using loops to iterate through a list of numbers and perform operations on each element. The program will calculate the sum, the average, and find the maximum and minimum values from a list of numbers.

### **Key Steps**:
1. **Create a List of Numbers**:  
   First, create a list of numbers either manually or by taking input from the user.

2. **Iterate through the List**:  
   Use a `for` loop to iterate over each element of the list and perform operations.

3. **Perform Calculations**:
   - Calculate the sum of all numbers in the list.
   - Calculate the average of the numbers.
   - Find the maximum and minimum values in the list.

4. **Output Results**:  
   After the loop completes, output the sum, average, maximum, and minimum values.

---

**Example**:

### 1.Create a list of numbers
```python
numbers = [10, 20, 30, 40, 50]
```

### 2.Initialize variables to store results
```python
sum_of_numbers = 0
max_number = numbers[0]
min_number = numbers[0]
```

### 3.Loop through the list to calculate sum, max, and min
```python
for number in numbers:
    sum_of_numbers += number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number
```

###  4.Calculate the average
```python
average = sum_of_numbers / len(numbers)
```

### 5.Output the results
```python
print("Sum:", sum_of_numbers)            # Output: Sum: 150
print("Average:", average)               # Output: Average: 30.0
print("Maximum:", max_number)            # Output: Maximum: 50
print("Minimum:", min_number)            # Output: Minimum: 10
```
