''''
Author: Joe George
Date: 20 November 2024
'''

numbers = [1,2,3,4,5,6,7,8,9,10]

sum = 0
largest_number = numbers[0]
smallest_number = numbers[0]


for number in numbers:
    sum += number                           # adds number to sum so as to calcuate average in the future
    if number > largest_number:             
        largest_number = number             # determines largest number
    if number < smallest_number:            
        smallest_number = number            # determines smallest number

# Calculates the average
average = sum/len(numbers)            

# Prints sum, average, largest and smalles numbers respectively
print(f"Sum: {sum}")            
print(f"Average: {average}")               
print(f"Largest Number: {largest_number}")            
print(f"Smallest Number: {smallest_number}")
