list1 = [10,2,3,4,2,23,4,45,45,56,23,1,23,4,32]
unique_set = sorted(set(list1))

print(unique_set)

grades=(27,27,29,30)
avg_grades = sum(grades) / len(grades)

print(avg_grades)

students1 = {"Joe_G", "Joe_M"}
students2 = {"Job"}
students = students1 & students2


student_grades = {
    "Arbitran": (85, 90, 78),
    "Barbie": (88, 76, 92),
    "Callux": (80, 85, 88),
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average:.2f}")
