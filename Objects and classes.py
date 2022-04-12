class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.av_grades_student = 0

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades_lecturer:
                lecturer.grades_lecturer[course] += [grade]
            else:
                lecturer.grades_lecturer[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            return
        return self.av_grades_student < other.av_grades_student

    def __str__(self):
        self.av_grades_course = 0
        for course in self.grades:
            self.av_grades_course += sum(self.grades[course]) / len(self.grades[course])
        self.av_grades_student = self.av_grades_course / len(self.grades)
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self.av_grades_student}\nКурсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        return text


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades_lecturer = {}
        self.av_grades_lecturer = 0

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return
        return self.av_grades_lecturer < other.av_grades_lecturer

    def __str__(self):
        self.av_grades_course = 0
        self.av_grades_lecturer = 0
        for course in self.grades_lecturer:
            self.av_grades_course += sum(self.grades_lecturer[course]) / len(self.grades_lecturer[course])
        self.av_grades_lecturer = self.av_grades_course / len(self.grades_lecturer)
        text = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.av_grades_lecturer}'
        return text


class Reviewer(Mentor):

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        text = f'Имя: {self.name}\nФамилия: {self.surname}'
        return text


# Аргументы
student1 = Student('Anna', 'Zen', 'man')
student1.courses_in_progress += ['Python', 'Git']
student1.finished_courses += ['Введение в программирование']
student2 = Student('Helena', 'Nilson', 'man')
student2.courses_in_progress += ['Python', 'Git']
student2.finished_courses += ['Введение в программирование']

lecturer1 = Lecturer('Yulia', 'Semenova')
lecturer1.courses_attached += ['Python', 'Git']
lecturer2 = Lecturer('Nikolay', 'Pavlov')
lecturer2.courses_attached += ['Python', 'Git']

reviewer1 = Reviewer('Artur', 'Miroshkin')
reviewer1.courses_attached += ['Python', 'Git']
reviewer2 = Reviewer('Ivan', 'Ivanov')
reviewer2.courses_attached += ['Python', 'Git']

student1.rate_lecturer(lecturer1, 'Python', 8)
student1.rate_lecturer(lecturer1, 'Git', 9)
student1.rate_lecturer(lecturer2, 'Python', 10)
student1.rate_lecturer(lecturer2, 'Git', 10)

student2.rate_lecturer(lecturer1, 'Python', 7)
student2.rate_lecturer(lecturer1, 'Git', 8)
student2.rate_lecturer(lecturer2, 'Python', 9)
student2.rate_lecturer(lecturer2, 'Git', 9)

reviewer1.rate_hw(student1, 'Python', 7)
reviewer1.rate_hw(student1, 'Git', 5)
reviewer1.rate_hw(student2, 'Python', 10)
reviewer1.rate_hw(student2, 'Git', 9)
reviewer2.rate_hw(student1, 'Python', 6)
reviewer2.rate_hw(student1, 'Git', 5)
reviewer2.rate_hw(student2, 'Python', 8)
reviewer2.rate_hw(student2, 'Git', 7)

print(reviewer1)
print(reviewer2)
print(lecturer1)
print(lecturer2)
print(student1)
print(student2)

print(student1 < student2)

print(lecturer1 < lecturer2)

students = [student1, student2]
course1 = 'Python'


def av_among_students(students, course):
    sum_grade = 0
    count = 0
    for student in students:
        sum_grade += sum(student.grades[course]) / len(student.grades[course])
        count += 1
    return round(sum_grade / len(students), 2)


print(av_among_students(students, course1))

lecturers = [lecturer1, lecturer2]
course2 = 'Git'


def av_among_lecturers(lecturers, course):
    sum_grade = 0
    count = 0
    for lecturer in lecturers:
        sum_grade += sum(lecturer.grades_lecturer[course]) / len(lecturer.grades_lecturer[course])
        count += 1
    return round(sum_grade / len(lecturers), 2)


print(av_among_lecturers(lecturers, course2))














