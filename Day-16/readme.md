# Day 16: Applying Sets, Lists, and Tuples in Python

## **Task**: Solve problems that require a combination of sets, lists, and tuples for efficient data management and operations.

**Description**:  
Today’s task challenges you to leverage the unique characteristics of sets, lists, and tuples in Python. You'll perform operations to filter data, maintain order, and avoid duplicates. These exercises will deepen your understanding of when and how to use these data types effectively.

---

## 1. Filtering Unique Data
You have a list of student IDs with duplicates. Convert it into a set to remove duplicates and then back into a sorted list.

```python
student_ids = [102, 101, 105, 102, 101, 103, 104, 105]
unique_sorted_ids = sorted(set(student_ids))
print("Unique and Sorted Student IDs:", unique_sorted_ids)
# Output: Unique and Sorted Student IDs: [101, 102, 103, 104, 105]
```

---

## 2. Using Tuples for Immutable Data
Create a tuple to represent the grades of a student for different subjects and calculate the average grade.

```python
grades = (85, 92, 78, 88, 90)
average_grade = sum(grades) / len(grades)
print("Grades:", grades)
print("Average Grade:", average_grade)
# Output: Grades: (85, 92, 78, 88, 90)
#         Average Grade: 86.6
```

---

## 3. Set Operations for Common Interests
Two groups of students attend workshops on Python and Data Science. Use set operations to find students who attend both workshops.

```python
python_students = {"Alice", "Bob", "Charlie", "Diana"}
data_science_students = {"Charlie", "Eve", "Diana", "Frank"}

common_students = python_students & data_science_students
print("Students attending both workshops:", common_students)
# Output: Students attending both workshops: {'Charlie', 'Diana'}
```

---

## 4. Combining Data Structures
Create a dictionary where the keys are student names and the values are tuples containing their grades. Then use a loop to print each student's average grade.

```python
student_grades = {
    "Alice": (85, 90, 78),
    "Bob": (88, 76, 92),
    "Charlie": (80, 85, 88),
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average:.2f}")
# Output: 
# Alice's Average Grade: 84.33
# Bob's Average Grade: 85.33
# Charlie's Average Grade: 84.33
```

---

**Summary**:  
- **Sets** are ideal for ensuring data uniqueness and performing operations like union or intersection.  
- **Lists** provide order and mutability, making them great for sorted data.  
- **Tuples** are immutable and can store related data compactly.

Use these problems to explore the versatility of Python’s data structures!
