number_of_students = int(input())
student_grades = {}

for data in range(number_of_students):
    name, grade = input().split()
    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(float(grade))
    # {'Peter': [5.2, 3.2], 'Mark': [5.5, 2.5, 3.46], 'Alex': [2.0, 3.0]}

for name, grades in student_grades.items():
    average_grade = sum(grades)/len(grades)
    grades_list = ' '.join(str(f"{grade:.2f}") for grade in grades)
    print(f"{name} -> {grades_list} (avg: {average_grade:.2f})")
