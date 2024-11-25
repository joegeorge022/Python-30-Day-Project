"""
AUTHOR : JOE MARTIN RINCE
DATE : 24-11-2024
"""

numbers = [10, 20, 30, 40, 50]
sum_of_numbers = 0
max_number = numbers[0]
min_number = numbers[0]
for number in numbers:
    sum_of_numbers += number
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

average = sum_of_numbers / len(numbers)

print("Sum:", sum_of_numbers)            # Output: Sum: 150
print("Average:", average)               # Output: Average: 30.0
print("Maximum:", max_number)            # Output: Maximum: 50
print("Minimum:", min_number)            # Output: Minimum: 10