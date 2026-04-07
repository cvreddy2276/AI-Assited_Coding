class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0 - 100
        
    def get_grade(self):
        return self.grade
