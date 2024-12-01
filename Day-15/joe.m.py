"""
AUTHOR : JOE MARTIN RINCE
DATE : 1-12-2024
"""

student_scores={"Alan":85,
                "Sam":90,
                "Bob":95}

def calculate_average(scores):
    total = sum(scores.values())
    count = len(scores)
    average = total / count if count > 0 else 0
    return average

average_score = calculate_average(student_scores)
print("Average Score:", average_score)  # Output: Average Score: 90.0

def find_highest_score(scores):
    highest_student = max(scores, key=scores.get)
    return highest_student, scores[highest_student]

highest_student, highest_score = find_highest_score(student_scores)
print(f"Highest Score: {highest_student} with {highest_score}")  # Output: Highest Score: Diana with 92
for student in student_scores:
    print(f"{student}: {student_scores[student]}")

for student, score in student_scores.items():
    print(f"{student} has a score of {score}.")

