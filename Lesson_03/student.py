class Student:

    def __init__(self, name, famy, age, course):
        self.name = name
        self.famy = famy
        self.age = age
        self.course = course

    def __str__(self):
        return f'{self.name} {self.famy}, {self.age} лет, курс : {self.course}'
