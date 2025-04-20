import pandas as pd
student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

for (student, score) in student_data_frame.iterrows():
    print(score.student)
    print(score.score)