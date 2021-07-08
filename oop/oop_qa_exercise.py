
class Students:

    def __init__(self, name, age, subject):
        self.name = name
        self.age = age
        self.subject = subject

    def average_score(self, num1, num2, num3):
        return f"student's name is: {self.name}, average score is {int((num1+num2+num3)/3)}"

jane = Students("Jane", "23", "Maths")
jimmy = Students("Jimmy", "26", "Chemistry")
laszlo = Students("Laszlo", "24", "Physics")

print(jimmy.average_score(50, 60, 70))
print(jane.average_score(76, 48, 88))
print(laszlo.average_score(86, 74, 34))