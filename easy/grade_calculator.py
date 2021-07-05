print('Welcome to grade calculator \n')

maths_mark = int(input('Please input your math mark:'))
chemistry_mark = int(input('Please input your math mark:'))
physics_mark = int(input('Please input your math mark:'))

average_grade = (maths_mark + chemistry_mark + physics_mark) / 3


grade = 'You failed'

if average_grade < 40:
    grade = 'You failed'
elif average_grade >= 40 and average_grade < 50:
    grade = 'D'
elif average_grade >= 50 and average_grade < 60:
    grade = 'C'
elif average_grade >= 60 and average_grade < 70:
    grade = 'B'
else:
    grade = 'A'

print(f'Your average score is : {average_grade}%')
print(f'You scored a grade of: {grade}')
