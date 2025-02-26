class CourseGroup:
    def __init__(self, student, classmate):
        self.student = student
        self.clma = classmate

    def __str__(self):
        classmate_str = ", ".join([str(classmate) for classmate in self.clma])
        return f'{self.student} одногруппники с: {classmate_str}'
