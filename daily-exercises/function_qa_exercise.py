student_name = input("Please enter your name:")
homework_points = int(input("Please enter your homework points /25:"))
assessment_points = int(input("Please enter your assessment points /50:"))
final_exam_points = int(input("Please enter your Final exam points /100:"))

def ict_avarege(homework_points, assessment_points, final_exam_points):
    percentage = ((homework_points * 4) + (assessment_points * 2) + final_exam_points) / 3
    # grade = ''
    # if percentage >= 80:
    #     grade == 'A'
    # elif percentage < 80 and percentage >= 70:
    #     grade == 'B'
    # elif percentage < 70 and percentage >= 60:
    #     grade == 'C'
    # elif percentage < 60 and percentage >= 50:
    #     grade == 'D'
    # else:
    #     grade == 'F'
    return f"Your average is {percentage} % and your grade is {grade}"


print(student_name)
print(ict_avarege(homework_points, assessment_points, final_exam_points))

