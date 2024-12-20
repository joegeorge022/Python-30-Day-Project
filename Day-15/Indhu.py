'''
AUTHOR:INDHU SUBASH
DATE:20-12-24
'''
Aryan=int(input("enter mark of Aryan:"))
Meera=int(input("enter mark of Meera: "))
Kuttappan=int(input("enter mark of Kuttappan: "))
student_score=({"Aryan":Aryan, "Meera":Meera,"Kuttappan":Kuttappan})
def average(i):
    total=sum(i.values())
    count=len(i)
    avg=total/count
    return avg
print("Average score:",average(student_score))
def find_highest_score(scores):
    highest_student= None
    highest_score=0
    for student,score in scores.items():
        if score> highest_score:
            highest_score=score
            highest_student=student
    return highest_student,highest_score
highest_student,highest_score=find_highest_score(student_score)
print(f"Highest score:{highest_student} with {highest_score}")
