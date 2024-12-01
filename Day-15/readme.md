# Day 15: Functions and Looping with Dictionaries

## **Task**: Explore functions that operate on dictionaries and practice looping through dictionaries to manipulate and retrieve data.

**Description**:  
In Python, functions can be defined to perform operations on dictionaries, making your code more modular and reusable. Additionally, understanding how to loop through dictionaries is crucial for processing data efficiently. Today’s task will focus on:

1. **Defining functions** that take dictionaries as arguments.
2. **Using loops** to iterate over keys, values, and key-value pairs in dictionaries.
3. Implementing beginner-friendly questions to reinforce your understanding.

---

##  1. Defining a Function to Calculate Average Scores
Create a function that takes a dictionary of student scores and returns the average score.

```python
def average(i):
    total = sum(i.values())        # Here the total value is set as the sum of all values
    count = len(i)                 # Here the total count is set to the number of values
    average = total/count          # Avg = total/count
    return average

print("Average Score:",average(student_scores))        # The function average() is used to find the average score.
```

## 2. Function to Find the Highest Score
Define a function that finds the student with the highest score.

```python
def find_highest_score(scores):
    highest_student = None
    highest_score = 0
    for student, score in scores.items():
        if score > highest_score:
            highest_score = score
            highest_student = student
    return highest_student, highest_score

highest_student, highest_score = find_highest_score(student_scores)
print(f"Highest Score: {highest_student} with {highest_score}")
```

3. Looping Through Keys and Values
Use a loop to print each student's name along with their score.

```python
for student in student_scores:
    print(f"{student}: {student_scores[student]}")
```

4. Looping Through Key-Value Pairs
You can also loop through key-value pairs directly using the items() method.

```python
for student, score in student_scores.items():
    print(f"{student} has a score of {score}.")
```

