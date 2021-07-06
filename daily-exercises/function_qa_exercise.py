student_name = input("Please enter your name:")
homework_points = int(input("Please enter your homework points /25:"))
assessment_points = int(input("Please enter your assessment points /50:"))
final_exam_points = int(input("Please enter your Final exam points /100:"))

def ict_avarege(homework_points, assessment_points, final_exam_points):
    percentage = ((homework_points * 4) + (assessment_points * 2) + final_exam_points) / 3
    return f"{percentage} %"


print(student_name)
print(ict_avarege(homework_points, assessment_points, final_exam_points))

