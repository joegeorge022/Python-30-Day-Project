# Day 11: Exploring Tuples and Sets in Python

## **Task**: Practice using tuples and sets to store and manipulate data.  

**Description**:  
In this task, you will work with **tuples** and **sets**, two important data structures in Python. Tuples are immutable and are often used to store fixed data, while sets are unordered collections of unique items.  

### **Key Steps**:  
1. **Create and Access Tuples**:  
   - Define a tuple containing elements of your choice.  
   - Access elements using indexing and slicing.  

2. **Manipulate Tuples**:  
   - Convert a tuple to a list, modify it, and convert it back to a tuple.  

3. **Work with Sets**:  
   - Create a set of unique numbers or strings.  
   - Add and remove elements from the set.  
   - Perform set operations like union, intersection, and difference.  

---

**Example**:  

# Tuples
```python
my_tuple = (10, 20, 30, 40)
print("Original Tuple:", my_tuple)  # Output: Original Tuple: (10, 20, 30, 40)
```

## 1.Accessing elements
```python
print("First Element:", my_tuple[0])       # Output: First Element: 10
print("Last Element:", my_tuple[-1])       # Output: Last Element: 40
```

## 2.Convert tuple to list, modify, and convert back
```python

my_list = list(my_tuple)
my_list.append(50)
my_tuple = tuple(my_list)
print("Modified Tuple:", my_tuple)         # Output: Modified Tuple: (10, 20, 30, 40, 50)
```

# Sets
```python
my_set = {10, 20, 30, 40}
print("Original Set:", my_set)             # Output: Original Set: {40, 10, 20, 30}
```

## 1.Add and remove elements
```python
my_set.add(50)
my_set.remove(20)
print("Updated Set:", my_set)              # Output: Updated Set: {40, 10, 50, 30}
```

## 2.Set Operations
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1.union(set2))          # Output: Union: {1, 2, 3, 4, 5, 6}
print("Intersection:", set1.intersection(set2)) # Output: Intersection: {3, 4}
print("Difference:", set1.difference(set2))     # Output: Difference: {1, 2}
```
