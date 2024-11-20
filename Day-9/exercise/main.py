student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
    }
student_grades ={}
for student in student_scores:
    score = student_scores[student]
    if 90> score <=100:
        student_grades[student] = "A+"
    elif 80> score <=90:
        student_grades[student] = "B+"
    elif 70< score <=80:
        student_grades[student] = "C+"
    elif 70<= score >=0:
        student_grades[student] = "Fail"


print(student_grades)