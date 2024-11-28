'''AUTHOR:GANESH
28/11/24'''


student_marks = {
    "Job": 90,
    "Bobz": 65,
    "Joe": 80
}

print("Bobz\'s Marks",student_marks["Bobz"])
print()

print("Joe's Marks",student_marks["Joe"])
print()

student_marks["Job"]=93
print("Updated Marks",student_marks)
print()

r=student_marks.pop("Bobz")
print("After Removing Bobz's Marks",r)
print()


for student,marks in student_marks.items():
    print("Student",student,"Marks",marks)
    
