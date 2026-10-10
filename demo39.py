class Teacher:
    def __init__(self, name):
        self.name = name
    def teach(self):
        print(self.name, "is teaching")
class Dept:
    def __init__(self, teacher):
        self.teacher = teacher
teacher1 = Teacher('Ram')
dept = Dept(teacher1)
dept.teacher.teach()
