'''AUTHOR:GANESH
DAY 16'''
student_ids=[101,105,102,104,104,103,106,109,110,102]
Student_IDs=sorted(set(student_ids))
print("The Student IDs",Student_IDs)
st=set(Student_IDs)
print(st)


grades=(85,76,98,34,56,87,23,45)
avg_grades=sum(grades)/len(grades)
print("Grades of Students:",grades)
print("AVerage marks:",avg_grades)
print()

student_grades = {
    "Joe m": (85, 90, 78),
    "Indhu": (88, 76, 92),
    "job thomas": (80, 85, 88),
}

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    print(f"{student}'s Average Grade: {average}")
