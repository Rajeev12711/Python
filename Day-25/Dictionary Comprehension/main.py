import random

names  = ["Anurag", 'Rupesh', 'Amit', 'Shivam', "Harsh", 'Ashish']

student = {name for name in names}
print(student)

student_score = {name:random.randint(0,100) for name in names }
print(student_score)

passed_student = {name : score for (name,score) in student_score.items() if score >=50}
print(passed_student)