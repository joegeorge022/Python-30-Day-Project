student_scores = {"Apple":9,"Mango":7,"Orange":8,"Watermelon":10}

def average(i):
    total = sum(i.values())        # Here the total value is set as the sum of all values
    count = len(i)                 # Here the total count is set to the number of values
    average = total/count          # Avg = total/count
    return average

print("Average Score:",average(student_scores))        # The function average() is used to find the average score.



def find_highest_score(scores):
    highest_student = None
    highest_score = 0
    for student, score in scores.items():
        if score > highest_score:
            highest_score = score
            highest_student = student
    return highest_student, highest_score

highest_student, highest_score = find_highest_score(student_scores)
print(f"Highest Score: {highest_student} with {highest_score}")



for student in student_scores:
    print(f"{student}: {student_scores[student]}")

for i,j in student_scores.items():
        print(f"{i} has a score of {j}.")
