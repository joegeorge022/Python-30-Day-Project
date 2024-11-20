# Day 10: Working with Loops and Lists

## Task: Use loops to manipulate and iterate over a list of numbers.

**Description**:  
In this task, you will practice using loops to iterate through a list of numbers and perform operations on each element. The program will calculate the sum, the average, and find the maximum and minimum values from a list of numbers.

### Key Steps:
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
{% highlight python linenos %}
# Create a list of numbers
numbers = [10, 20, 30, 40, 50]

# Initialize variables to store results
sum_of_numbers = 0
max_number = numbers[0]
min_number = numbers[0]

# Loop through the list to calculate sum, max, and min
for number in numbers:
    sum_of_numbers += number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

# Calculate the average
average = sum_of_numbers / len(numbers)

# Output the results
print("Sum:", sum_of_numbers)            # Output: Sum: 150
print("Average:", average)               # Output: Average: 30.0
print("Maximum:", max_number)            # Output: Maximum: 50
print("Minimum:", min_number)            # Output: Minimum: 10
{% endhighlight %}

