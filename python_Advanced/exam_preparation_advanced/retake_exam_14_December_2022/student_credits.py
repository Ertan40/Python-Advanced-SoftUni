def students_credits(*args):
    # ('Computer Science-12-300-250', 'Basic Algebra-15-400-200', 'Algorithms-25-500-490')
    # "{course name}-{credits}-{max test points}-{diyan's points}"
    student_info = {}
    sum_of_all = 0
    final_strings = []
    for info in args:
        # info = Algorithms-25-500-490
        data = info.split("-")
        course_name = data[0]
        credit = int(data[1])
        max_test_points = int(data[2])
        diyans_points = int(data[3])
        current_credit = float(((diyans_points / max_test_points) * 100) * credit / 100)
        if course_name not in student_info:
            student_info[course_name] = current_credit
            sum_of_all += current_credit
        # {'Computer Science': [10.000000000000002], 'Basic Algebra': [7.5], 'Algorithms': [24.5]}
    if sum_of_all >= 240:
        final_strings.append(f"Diyan gets a diploma with {sum_of_all:.1f} credits.")
    else:
        needed_credit = (240 - sum_of_all)
        final_strings.append(f"Diyan needs {needed_credit:.1f} credits more for a diploma.")

    for course_name, credit in sorted(student_info.items(), key=lambda x: -x[1]):
        final_strings.append(f"{course_name} - {credit:.1f}")

    return '\n'.join(final_strings)


print(
    students_credits(
        "Computer Science-12-300-250",
        "Basic Algebra-15-400-200",
        "Algorithms-25-500-490"
    )
)

print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)

print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)