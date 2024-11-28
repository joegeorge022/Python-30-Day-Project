no_of_students={
    "classA":70,
    "classB":71,
    "classC":72
}
print("number of student in classA=",no_of_students["classA"])
no_of_students["classB"]=73
no_of_students["classD"]=75
#no_of_students.pop("classB")
print(no_of_students)
for classdiv,students in no_of_students.items():
    print(classdiv,":",students)