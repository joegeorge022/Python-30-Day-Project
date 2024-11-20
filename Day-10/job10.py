"""
Author :Job Thomas Cherian
Date:13/11/24
"""
numbers=[1,2,3,4]
productOfNumbers=1
max_number=numbers[0]
min_number=numbers[0]
for number in numbers :
    productOfNumbers *= number
    if number >max_number:
        max_number=number
    if number<min_number:
        min_number=number
average = productOfNumbers/len(numbers)
print(productOfNumbers)
print(min(numbers))
print(max_number)
print(average)
