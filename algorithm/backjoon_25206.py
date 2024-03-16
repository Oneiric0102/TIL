import sys

total_credit = 0
total_grade = 0
grade_dict = {
    "A+": 4.5,
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0,
}
for i in range(20):
    grade_info = sys.stdin.readline().split()
    if grade_info[2] == "P":
        pass
    else:
        total_credit += float(grade_info[1])
        total_grade += float(grade_info[1]) * grade_dict[grade_info[2]]

print(total_grade / total_credit)
