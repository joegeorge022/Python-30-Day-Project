# Day 9: Creating Custom Lists

## **Task**: Implement a Python program to create a list with user-specified elements and types.

**Description**:  
In this task, you will create a Python program that allows a user to build a custom list by specifying the number of elements and their types (strings or numbers). This program introduces concepts of user input handling, loops, and data type operations.

### **Key Steps**:
1. **User Input for List Length**:  
   The user specifies how many elements the list will have. Use the `int` function to ensure the input is a number.

2. **Loop for Adding Elements**:  
   Use a `while` loop to add the specified number of elements to the list.

3. **Type Selection**:  
   - If the user selects "S", they will input a string.  
   - If the user selects "N", they will input a number.  
   - Handle invalid inputs gracefully.

4. **Output the Final List**:  
   Once all elements are added, print the complete list.

---

**Example**:
```python
# User specifies the length of the list
limit = int(input("Enter length of list: "))

# Initialize the counter and the list
i = 0
L = []

# Loop to collect elements
while i < limit:
    ty = input("Enter data type (S for String / N for Number): ").upper()
    
    if ty == "S":
        element = input("Enter the string element: ")
        L.append(element)
        i += 1
    elif ty == "N":
        try:
            element = int(input("Enter the number element: "))
            L.append(element)
            i += 1
        except ValueError:
            print("Invalid input! Please enter a number.")
    else:
        print("Invalid type! Please enter 'S' or 'N'.")
    
# Output the final list
print("Final List:", L)

