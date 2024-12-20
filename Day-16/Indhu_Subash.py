"""
AUTHOR : INDHU SUBASH
DATE : 20-12-2024
"""
student_ids = [102, 101, 105, 102, 101, 103, 104, 105]
unique_sorted_ids = sorted(set(student_ids))
unique_sorted_ids=set(unique_sorted_ids)
print("Unique and Sorted Student IDs:", unique_sorted_ids)

grades = (100,98,95,87,93)
average_grade = sum(grades) / len(grades)
print(f"Grades : {grades}")
print("Average Grade:", average_grade)

python_students = {"Appu", "Abhijith", "Unni", "Abhishek"}
machine_learning_students = {"Unni", "Eve", "Abhishek", "Alice"}

common_students = python_students & machine_learning_students
print("Students attending both workshops:", common_students)

student_grades = {
    "Appu": (85, 90, 78),
    "Abhijith": (88, 76, 92),
    "Unni": (80, 85, 88),
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average:.2f}")