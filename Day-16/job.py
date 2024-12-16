customers=["cust1","cust2","cust3","cust1","cust3","cust2"]
unique_customers=sorted(set(customers))
print("unique and sorted customers:",unique_customers)
# using tuples for immutable data
grades = (94,82,82,34,93)
average_grade=sum(grades)/len(grades)
print(f"grades:{grades}")
print(f"average grade:{average_grade}")
# set opertions

python_students={"alice","boby","diana","charlie"}
java_students={"charlies","eve","diana,frank"}
commom_student=python_students or java_students
print(commom_student)
