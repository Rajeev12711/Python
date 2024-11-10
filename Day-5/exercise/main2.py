student_score = input("Input a list of student ").split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
print(student_score)

highest=0
for i in student_score:
    if i > highest:
        highest=i

print("The highest scor ein class", i)