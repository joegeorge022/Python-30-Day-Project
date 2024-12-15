alice =int(input("enter mark of alice:"))
jack=int(input("enter mark of jack: "))
sid=int(input("enter mark of sid: "))
student_score=({"alice":alice, "jack":jack,"sid":sid})
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

