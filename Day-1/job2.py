'''Author: Job Thomas Cherian
   Day 1
   program for name and age'''

Name=input("Enter your name:")
Age=int(input("Enter your age:"))

is_student=True

print(f"Hello {Name}")
print(f"hey {Name} you are {Age} old now")
print(f"are you a student? ans:{is_student}")

if is_student:
    print("he is a student")
else:
    print("he is not a student")
