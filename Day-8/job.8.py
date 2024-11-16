"""
Authour:Job Thomas Cherian
Date: 16/11/24
"""
fruits=["orange","apple","cherry","grapes","pappaya"]
for fruit in fruits:
   if fruit ==  "cherry":
       break
   print(fruit,end=" ")

print()


for fruit in fruits:
 if "r" not in fruit:
     continue
 print(fruit,end=" ")
print()

for fruit in fruits:
     if fruit =="grapes":
      pass
     print(fruit,end=" ")


