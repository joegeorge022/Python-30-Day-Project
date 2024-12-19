# Day 23: Demonstrating List Operations

## **Task**: Practice various list operations using Python.

**Description**:  
Today, you will explore how to manipulate lists using various built-in methods. Lists are one of the most versatile data structures in Python, and understanding these methods will help you manage collections of data efficiently.

You will implement a function `list_operations_demo()` that demonstrates the following operations step-by-step:

### Operations to Perform:

- **`append()`**: Add an element to the end of a list.
- **`extend()`**: Extend a list with elements from another list.
- **`insert()`**: Insert an element at a specified index.
- **`remove()`**: Remove the first occurrence of a specific value.
- **`pop()`**: Remove an element by its index.
- **`index()`**: Find the index of the first occurrence of a value.
- **`count()`**: Count the occurrences of a specific value in the list.
- **`reverse()`**: Reverse the list.
- **`sort()`**: Sort the list in ascending order.
- **`clear()`**: Remove all elements from the list.

---

## **Expected Outputs**

### Starting List
`[10, 20, 30, 40]`

### Step-by-Step Results

1. **After `append(50)`**:  
`[10, 20, 30, 40, 50]`

2. **After `extend([60, 70])`**:  
`[10, 20, 30, 40, 50, 60, 70]`

3. **After `insert(2, 25)`**:  
`[10, 20, 25, 30, 40, 50, 60, 70]`

4. **After `remove(30)`**:  
`[10, 20, 25, 40, 50, 60, 70]`

5. **After `pop(3)`**:  
`[10, 20, 25, 50, 60, 70]`  
(Removed element: `40`)

6. **Index of `50`**:  
`3`

7. **Count of `20`**:  
`1`

8. **After `reverse()`**:  
`[70, 60, 50, 25, 20, 10]`

9. **After `sort()`**:  
`[10, 20, 25, 50, 60, 70]`

10. **After `clear()`**:  
`[]`

---

## **Conclusion**

Lists in Python offer a wide range of methods to perform various operations efficiently. By mastering these methods, you can handle dynamic datasets with ease. Today’s task reinforces how to manipulate and transform lists step-by-step, ensuring you’re well-equipped to tackle real-world problems involving collections of data.

