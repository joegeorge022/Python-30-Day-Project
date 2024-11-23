number=[1,2,3,4,5,6,7,8,]

for num in number:
    if num == 4:
        break
    print(num)

for num in number:
    if num==6:
        continue
    print(num)

for num in number:
    if num==3:
        pass
    print(num)