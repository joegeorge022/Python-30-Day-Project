'''
AUTHOR:INDHU SUBASH
'''

student_scores={"Abin":85,
                "Aryan":90,
                "Aravind":95}

print("Aryan's score:",student_scores["Aryan"])
student_scores["Diana"] = 89
print("Updated Dictionary:", student_scores)
student_scores["Aravind"]=98
print("Modified Score for Aravind:", student_scores["Aravind"])
removed_score = student_scores.pop("Aravind")
print("Removed Aravind's Score:", removed_score)
print("Dictionary after removal:", student_scores)

for student, score in student_scores.items():
    print(f"{student}: {score}")