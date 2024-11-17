class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        self.average_rating = float()

    def __str__(self):
        grades_count = 0
        for item in self.grades:
            grades_count += len(self.grades[item])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.average_rating}\n' \
               f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {', '.join(self.finished_courses)}'

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Ошибка')
            return
        return self.average_rating < other.average_rating


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.average_rating = float()
        self.grades = {}

    def __str__(self):
        grades_count = 0
        for i in self.grades:
            grades_count += len(self.grades[i])
        self.average_rating = round(sum(map(sum, self.grades.values())) / grades_count, 2)
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self.average_rating}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Ошибка')
            return
        return self.average_rating < other.average_rating


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
        return f'Имя: {self.name}\nФамилия: {self.surname}'

lecturer_1 = Lecturer('John', 'Doe')
lecturer_1.courses_attached += ['Python']
lecturer_2 = Lecturer('Mary', 'Sue')
lecturer_2.courses_attached += ['Git']

reviewer_1 = Reviewer('Franz', 'Ferdinand')
reviewer_1.courses_attached += ['Python']
reviewer_1.courses_attached += ['Git']
reviewer_2 = Reviewer('Gugu', 'Gaga')
reviewer_2.courses_attached += ['Python']
reviewer_2.courses_attached += ['Git']

student_1 = Student('Bronya', 'Zaychik', 'Female')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']
student_2 = Student('Gura', 'Gawr', 'Female')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']


student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_1, 'Python', 10)
student_1.rate_lecturer(lecturer_2, 'Git', 5)
student_1.rate_lecturer(lecturer_2, 'Git', 7)

student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_1, 'Python', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 10)
student_2.rate_lecturer(lecturer_2, 'Git', 8)

reviewer_1.rate_hw(student_1, 'Python', 8)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 9)

reviewer_1.rate_hw(student_2, 'Python', 7)
reviewer_1.rate_hw(student_2, 'Python', 10)
reviewer_1.rate_hw(student_2, 'Git', 5)
reviewer_1.rate_hw(student_2, 'Git', 10)

reviewer_2.rate_hw(student_1, 'Python', 8)
reviewer_2.rate_hw(student_1, 'Python', 9)
reviewer_2.rate_hw(student_1, 'Git', 7)
reviewer_2.rate_hw(student_1, 'Git', 9)

reviewer_2.rate_hw(student_2, 'Python', 8)
reviewer_2.rate_hw(student_2, 'Python', 7)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)

print(f'Студенты:\n1) {student_1}\n2) {student_2}')
print()
print(f'Лекторы:\n1) {lecturer_1}\n2) {lecturer_2}')
print()
print(f'Проверяющие:\n1) {reviewer_1}\n2) {reviewer_2}')
print()

# Результат сравнения студентов и лекторов по средним оценкам
print(f'Средний балл за ДЗ у {student_1.name} {student_1.surname} ({student_1.average_rating}) выше, чем у {student_2.name} {student_2.surname} ({student_2.average_rating}): {student_1.average_rating > student_2.average_rating}')
print(f'Средний балл за ДЗ у {student_1.name} {student_1.surname} ({student_1.average_rating}) ниже, чем у {student_2.name} {student_2.surname} ({student_2.average_rating}): {student_1.average_rating < student_2.average_rating}')
print()
print(f'Средний балл за лекции у {lecturer_1.name} {lecturer_1.surname} ({lecturer_1.average_rating}) ниже, чем у {lecturer_2.name} {lecturer_2.surname} ({lecturer_2.average_rating}): {lecturer_1.average_rating < lecturer_2.average_rating}')
print(f'Средний балл за лекции у {lecturer_1.name} {lecturer_1.surname} ({lecturer_1.average_rating}) выше, чем у {lecturer_2.name} {lecturer_2.surname} ({lecturer_2.average_rating}): {lecturer_1.average_rating > lecturer_2.average_rating}')
print()

# Функции расчета средних оценок по дисциплинам для студентов и для лекторов
student_list = [student_1, student_2]
lecturer_list = [lecturer_1, lecturer_2]

def student_rating(student_list, course_name):
    grades_total = 0
    grades_count = 0
    for student in student_list:
        if course_name in student.courses_in_progress:
            grades_total += student.average_rating
        grades_count += 1
        average_for_all = grades_total / grades_count
        return f'{average_for_all:.2f}'

def lecturer_rating(lecturer_list, course_name):
    grades_total = 0
    grades_count = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.courses_attached:
            grades_total += lecturer.average_rating
            grades_count += 1
    average_for_all = grades_total / grades_count
    return f'{average_for_all:.2f}'

print(f"Средняя оценка всех студентов по курсу Python: {student_rating(student_list, 'Python')}")
print(f"Средняя оценка всех студентов по курсу Git: {student_rating(student_list, 'Git')}")
print(f"Средняя оценка всех лекторов по курсу Pytnon: {lecturer_rating(lecturer_list, 'Python')}")
print(f"Средняя оценка всех лекторов по курсу Git: {lecturer_rating(lecturer_list, 'Git')}")