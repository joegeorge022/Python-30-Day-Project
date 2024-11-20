"""
Custom List Generator
Author: Joe George
"""

limit = int(input("Enter the size of the list: "))

count = 0
custom_list = []

while count < limit:
    data_type = input("Enter data type (S for String / N for Number): ").upper()  #.upper() makes sure lower case is also accepted

    if data_type == "S": 
        value = input("Enter a text value: ")                  
        custom_list.append(value)                              #Adds the inserted value to the list
        count += 1                                             #Adds +1 count
    elif data_type == "N":
            value = int(input("Enter a numerical value: "))
            custom_list.append(value)
            count += 1
    else:
        print("Invalid choice! Please enter 'S' or 'N'.")

print(f"Your Custom List is {custom_list}")
