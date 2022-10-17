class Student:

  def __init__(self, name, surname, gender):
    self.name = name
    self.surname = surname
    self.gender = gender
    self.finished_courses = []
    self.courses_in_progress = []
    self.grades = {}
    self.average_grade = 0

  def add_courses(self, course_name):
    self.finished_courses.append(course_name)

  def rate_lecturer(self, lecture, course, grade):
    if isinstance(lecture, Lecturer) and course in self.finished_courses and grade <= 10 and course in lecture.courses_attached:
      #if course not in self.finished_courses:
      lecture.grade_to_lecturer.update({course: grade})
      #else:
      #Lecturer.grade_to_lecturer[course] += [grade]
    else:
      return 'Ошибка'

  def average(self, student):
    self.student = student
    summa = 0
    for item in self.grades.values():
      summa += item
    average_grade = summa / len(self.grades)
    self.average_grade = average_grade
    return average_grade

# возможность сравнения

  def __lt__(self, other):
    if not isinstance(other, Student):
      print('Not a student!')
      return
    return self.average_grade < other.average_grade


#метод который позволяет возвращать след значение при применении print

  def __str__(self):
    res = (
      f'Имя: {self.name} \n Фамилия:{self.surname} \nСредняя оценка за лекции:{self.average_grade} \nКурсы в процессе изучения: {(",").join(map(str,self.courses_in_progress))} \nЗавершенные курсы: {(",").join(map(str,self.finished_courses))}'
    )
    return res


class Mentor:

  def __init__(self, name, surname):
    self.name = name
    self.surname = surname
    self.courses_attached = []


class Lecturer(Mentor):
  grade_to_lecturer = {}
  average_grade = 0

  def _average(self, lecturer):
    self.lecturer = lecturer
    summa = 0
    for item in self.grade_to_lecturer.values():
      summa += item
    average_grade = summa / len(self.grade_to_lecturer)
    self.average_grade = average_grade
    return self.average_grade

  # метод который позволяет возвращать след значение при применении print
  def __str__(self):
    res = f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекции: {self.average_grade}'
    return res


# возможность сравнения

  def __lt__(self, other):
    if not isinstance(other, Lecturer):
      print('Not a lecture!')
      return
    return self.average_grade < other.average_grade


class Reviewer(Mentor):
  pass

  def rate_hw(self, student, course, grade):
    if isinstance(
        student, Student
    ) and course in self.courses_attached and course in student.courses_in_progress or course in student.finished_courses:
      #student.grades.update({course: grade})
      if course in student.grades:
        student.grades[course] += [grade]
      else:
        student.grades[course] = [grade]
    else:
      return 'Ошибка'


#метод который позволяет возвращать след значение при применении print

  def __str__(self):
    res = f'Имя: {self.name} \n Фамилия:{self.surname}'
    return res

student1 = Student('Ruoy', 'Eman', 'man')
student1.finished_courses += ['Python']
student2 = Student('Bob', 'Lion', 'man')
student2.finished_courses += ['Python']

lecturer1 = Lecturer('Some', 'Buddy')
lecturer1.courses_attached += ['Python']
lecturer1.courses_attached += ['math']

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer1, 'math', 8)
student1.rate_lecturer(lecturer1, 'Python', 10)

reviewer1 = Reviewer('Oleg', 'Davydov')
reviewer1.rate_hw(student1, 'Python', 10)
reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Python', 10)

#сделать список подсчета средней оценки по всем студентам,
# т.е. сами создаем студентов и помещаем их в список, и далее первым циклом перебираем студентов,
# вторым циклом перебираем словарь их оценок, чтобы за конкретный курс - следовала конкретная оценка, чтобы по ним посчитать среднюю оценку


def average_all_students(student_list, course):
    count_grades = []
    for student in student_list:
        if isinstance(student, Student):
            count_grades += student.grades.get(course)
            len_ = len(count_grades)
            summa_ = sum(count_grades)
            average = summa_ / len_
    return round(average, 2)

student_list = [student1, student2]
course = 'Python'

print(average_all_students(student_list, course))
