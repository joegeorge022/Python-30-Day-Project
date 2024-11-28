'''AUTHOR:GANESH
28/11/24'''

numbers=[23,45,64,76,5,32,67,99,8]
max_num=numbers[0]
min_num=numbers[0]
sum_of_numbers=0
for number in numbers:
    sum_of_numbers+=number
    if number>max_num:
        max_num=number
    elif number<min_num:
        min_num=number

avg_nums=sum_of_numbers/len(numbers)
print("Largest number",max_num)
print("Smallest number",min_num)
print("Average number",avg_nums)
