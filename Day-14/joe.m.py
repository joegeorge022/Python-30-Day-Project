"""
AUTHOR : JOE MARTIN RINCE
DATE : 28-11-2024
"""

student_scores={"Alan":85,
                "Sam":90,
                "Bob":95}

print("Sam's score:",student_scores["Sam"])
student_scores["Diana"] = 92
print("Updated Dictionary:", student_scores)
student_scores["Bob"]=96
print("Modified Score for Bob:", student_scores["Bob"])

removed_score = student_scores.pop("Bob")
print("Removed Bob's Score:", removed_score)
print("Dictionary after removal:", student_scores)

for student, score in student_scores.items():
    print(f"{student}: {score}")
