from student import Student
from coursgroup import CourseGroup

best_student = Student('Степан', 'Семенов', 35, 'Колоноскопия')
clma1 = Student('Иван', 'Иванов', 6, 'Колоноскопия')
clma2 = Student('Егор ', 'Егоров', 15, 'Колоноскопия')
clma3 = Student('Дмитрий ', 'Дмитриев', 66, 'Колоноскопия')
clma4 = Student('Семен', 'Степанов', 35, 'Колоноскопия')
clma5 = Student('Мария', 'ПростоМария', 18, 'Колоноскопия')

coursgroup = CourseGroup(best_student, [clma1, clma2, clma3, clma4, clma5])
print(coursgroup)
