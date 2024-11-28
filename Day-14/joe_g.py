students = {
    "Joe": "George",
    "Job": "Thomas",
}

print(students ["Joe"])          # Prints the value associated with the key "Joe"

students["Ganesh"] = "Chandran"  # Added Ganesh✌️

students ["Joe"] = "Martin"      # Changed George to Martin 

students.pop("Job")              # Removes Job🥲

students["Job"] = "Thomas"       # Adds Job again😁

print(students)      

print()                          # Leaves an empty line

for first_name, last_name in students.items():
    print(f"{first_name}: {last_name}")
