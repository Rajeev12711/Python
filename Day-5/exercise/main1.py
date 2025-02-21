student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total =0
for height in student_heights:
    total = total +  height


num =0
for students in student_heights:
    num =num + 1

avg=total/num
print(avg)