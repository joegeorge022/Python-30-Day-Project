# Day 14: Introduction to Dictionaries 

## **Task**: Explore and manipulate dictionaries to work with key-value pairs.  

**Description**:  
A dictionary in Python is a collection of key-value pairs, where each key is unique. Dictionaries are mutable, allowing you to update, add, or remove items dynamically.  

In today’s task, you will:  
1. **Create dictionaries** to store data in key-value pairs.  
2. **Access and modify elements** using keys.  
3. Use methods to **add, remove, and retrieve items**.  
4. Perform operations like iterating over keys and values.  

---

##  1.Creating a dictionary
Define a dictionary with key-value pairs to store related data.
```python
student_scores = {
    "Alice": 85,
    "Bob": 90,
    "Charlie": 78
}
```
##  2.Accessing elements
Retrieve the value associated with a specific key in the dictionary.
```python
print("Alice's Score:", student_scores["Alice"])  # Output: Alice's Score: 85
```
##  3.Adding a new key-value pair
Add a new key and its corresponding value to the dictionary.
```python
student_scores["Diana"] = 92
print("Updated Dictionary:", student_scores)  # Output: Updated Dictionary: {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'Diana': 92}
```
##  4.Modifying an existing value
Update the value of a specific key in the dictionary.
```python
student_scores["Alice"] = 88
print("Modified Score for Alice:", student_scores["Alice"])  # Output: Modified Score for Alice: 88
```
##  5.Removing a key-value pair
Remove a key and its associated value using the pop() method.
```python
removed_score = student_scores.pop("Charlie")
print("Removed Charlie's Score:", removed_score)  # Output: Removed Charlie's Score: 78
print("Dictionary after removal:", student_scores)  # Output: {'Alice': 88, 'Bob': 90, 'Diana': 92}
```
##  6.Iterating through the dictionary
Loop through key-value pairs to process or display the dictionary's contents.
```python
for student, score in student_scores.items():
    print(f"{student}: {score}")
    # Output: Alice: 88, Bob: 90, Diana: 92
```
