# Day 10: Introduction to Sets

## **Task**: Explore the unique and unordered nature of sets in Python.

**Description**:  
Sets in Python are unordered collections of unique elements. They are useful for storing distinct items and performing operations like unions, intersections, and differences. Sets are defined using curly braces `{}` or the `set()` constructor.

### **Key Points**:
1. **Creating Sets**:  
   ```python
   # Empty set
   empty_set = set()

   # Set with elements
   sample_set = {1, 2, 3, "Python", 3.14}
   ```

2. **Unique Elements**:  
   Sets automatically remove duplicate entries:  
   ```python
   duplicate_set = {1, 2, 2, 3}
   print(duplicate_set)  # Output: {1, 2, 3}
   ```

3. **Set Operations**:  
   - Union: `set1 | set2`  
   - Intersection: `set1 & set2`  
   - Difference: `set1 - set2`  
   - Symmetric Difference: `set1 ^ set2`

4. **Adding and Removing Elements**:  
   ```python
   sample_set.add(10)      # Add an element
   sample_set.remove(1)    # Remove an element
   sample_set.discard(20)  # Remove without error if not present
   ```

5. **Membership Testing**:  
   ```python
   print(3 in sample_set)  # Output: True
   ```

---

**Example**:
```python
# Create two sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Set operations
print("Union:", set1 | set2)             # Output: Union: {1, 2, 3, 4, 5, 6}
print("Intersection:", set1 & set2)      # Output: Intersection: {3, 4}
print("Difference (set1 - set2):", set1 - set2)  # Output: Difference: {1, 2}
print("Symmetric Difference:", set1 ^ set2)  # Output: Symmetric Difference: {1, 2, 5, 6}

# Modifying sets
set1.add(10)
set1.remove(2)
print("Modified Set:", set1)             # Output: Modified Set: {1, 3, 4, 10}
```

**Challenge**:
1. Create a set with at least 7 elements, including duplicates, and observe the result.
2. Perform and print the union, intersection, and difference with another set.
3. Add a new element to the set and remove an existing one.
4. Check if a specific value exists in your set using membership testing.

Sets are an efficient way to manage unique data and perform mathematical set operations!
