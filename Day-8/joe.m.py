"""
AUTHOR : JOE MARTIN RINCE
DATE : 15-11-2024
"""

nums=[1,2,3,4,5,6,7,8,]

for num in nums:
    if num == 3:
        break
    print(num)



for num in nums:
    if num==5:
        continue
    print(num)


for num in nums:
    if num==5:
        pass
    print(num)