students_score = input("Enter a list of students score: ").split()
for n in range(0, len(students_score)):
    students_score[n] = int(students_score[n])
print(students_score)

highest=0
for i in students_score:
    if i > highest:
        highest=i

print("The highest score in class", highest)