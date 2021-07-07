
def grade_calculator(maths_mark, chemistry_mark, physics_mark):
    average_grade = int((maths_mark + chemistry_mark + physics_mark) / 3)
    results = {
        70 : 'A',
        60 : 'B',
        50 : 'C',
        40 : 'D'
    }
    for boundary, grade in results.items():
        if average_grade >= boundary:
            return f'Your average score is : {average_grade} You scored a grade of: {grade}'
    else:
        return f'Your average score is : {average_grade}. You failed'
    

if __name__ == "__main__":
    print('Welcome to grade calculator \n')

    maths_mark = int(input('Please input your math mark:'))
    chemistry_mark = int(input('Please input your math mark:'))
    physics_mark = int(input('Please input your math mark:'))

    print(grade_calculator(maths_mark, chemistry_mark, physics_mark))