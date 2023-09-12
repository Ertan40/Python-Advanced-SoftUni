# ------------------------ score: 93 -----------------------------------
def gather_credits(number_of_credits, *args):
    courses = []
    max_credits = 0
    for info in args:
        course_name = info[0]
        course_credits = info[1]

        if course_name not in courses:
            courses.append(course_name)
            max_credits += course_credits
            if max_credits >= number_of_credits:
                break

    credits_shortage = abs(number_of_credits - max_credits)

    if max_credits < number_of_credits:
        return f"You need to enroll in more courses! You have to gather {credits_shortage} credits more."

    return f"Enrollment finished! Maximum credits: {max_credits}.\nCourses: {', '.join(sorted(courses))}"


print(gather_credits(
    80,
    ("Basics", 27),
))

print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))


print(gather_credits(
    60,
    ("Basics", 27),
    ("Fundamentals", 27),
    ("Advanced", 30),
    ("Web", 30)
))