"""
AUTHOR : JOE Martin RINCE
DATE : 13-12-2024
"""
student_ids = [102, 101, 105, 102, 101, 103, 104, 105]
unique_sorted_ids = sorted(set(student_ids))
unique_sorted_ids=set(unique_sorted_ids)
print("Unique and Sorted Student IDs:", unique_sorted_ids)

grades = (100,98,95,87,93)
average_grade = sum(grades) / len(grades)
print(f"Grades : {grades}")
print("Average Grade:", average_grade)

python_students = {"Alice", "Bob", "Charlie", "Diana"}
data_science_students = {"Charlie", "Eve", "Diana", "Frank"}

common_students = python_students & data_science_students
print("Students attending both workshops:", common_students)

student_grades = {
    "Alice": (85, 90, 78),
    "Bob": (88, 76, 92),
    "Charlie": (80, 85, 88),
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average:.2f}")
