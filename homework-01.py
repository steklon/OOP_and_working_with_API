class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):

        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.gpa()}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def rate_lecturer(self, lecturer, course, grade):
        if 0 < grade <= 10:
            if ((isinstance(lecturer, Lecturer) and course in lecturer.courses_attached
                 and course in self.courses_in_progress)):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Ошибка'
        else:
            return 'Ошибка'

    def gpa(self):
        sum_ = 0
        quantity = 0
        for course in self.grades:
            # print(sum(self.grades[course]))
            sum_ += sum(self.grades[course])
            quantity += len(self.grades[course])
        average = sum_ / quantity
        return round(average, 1)

    def __lt__(self, other):
        return self.gpa() < other.gpa()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.gpa()}')

    def __lt__(self, other):
        return self.gpa() < other.gpa()

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def gpa(self):
        sum_ = 0
        quantity = 0
        for course in self.grades:
            sum_ = sum(self.grades[course])
            quantity = len(self.grades[course])
        average = sum_ / quantity
        return round(average, 1)


class Reviewer(Mentor):
    def __str__(self):
        return (f'Имя: {self.name}\n'
                f'Фамилия: {self.surname}')

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


dmitry_student = Student('Дмитрий', 'Черепов', 'мужской')
dmitry_student.courses_in_progress += ['Python', 'JavaScript']
dmitry_student.finished_courses += ['Введение в программирование']

anton_student = Student('Антон', 'Антонов', 'man')
anton_student.courses_in_progress += ['Python', 'JavaScript']
anton_student.finished_courses += ['Введение в программирование']

maxim_reviewer = Reviewer('Максим', 'Смирнов')
maxim_reviewer.courses_attached += ['Python']

evgeny_reviewer = Reviewer('Евгений', 'Игнатов')
evgeny_reviewer.courses_attached += ['JavaScript']

ivan_lecturer = Lecturer('Иван', 'Иванов')
ivan_lecturer.courses_attached += ['Python']

igor_lecturer = Lecturer('Игорь', 'Михайлович')
igor_lecturer.courses_attached += ['JavaScript']

maxim_reviewer.rate_hw(dmitry_student, 'Python', 8)
maxim_reviewer.rate_hw(dmitry_student, 'Python', 7)
maxim_reviewer.rate_hw(anton_student, 'Python', 9)
maxim_reviewer.rate_hw(anton_student, 'Python', 6)

evgeny_reviewer.rate_hw(dmitry_student, 'JavaScript', 6)
evgeny_reviewer.rate_hw(dmitry_student, 'JavaScript', 5)
evgeny_reviewer.rate_hw(anton_student, 'JavaScript', 10)
evgeny_reviewer.rate_hw(anton_student, 'JavaScript', 7)

dmitry_student.rate_lecturer(ivan_lecturer, 'Python', 10)
dmitry_student.rate_lecturer(ivan_lecturer, 'Python', 8)
dmitry_student.rate_lecturer(igor_lecturer, 'JavaScript', 9)
dmitry_student.rate_lecturer(igor_lecturer, 'JavaScript', 7)

anton_student.rate_lecturer(ivan_lecturer, 'Python', 9)
anton_student.rate_lecturer(ivan_lecturer, 'Python', 10)
anton_student.rate_lecturer(igor_lecturer, 'JavaScript', 6)
anton_student.rate_lecturer(igor_lecturer, 'JavaScript', 8)

print(anton_student, '\n')
# print(maxim_reviewer)
# print(igor_lecturer)
# print(anton_student > dmitry_student)

students_list = [dmitry_student, anton_student]


def student_scores(students, course_name):
    sum_ = 0
    quantity = 0
    for student_ in students:
        for course, grade in student_.grades.items():
            if course == course_name:
                sum_ += sum(grade)
                quantity += len(grade)
    average = sum_ / quantity
    return round(average, 1)


print(f'Средняя оценка за домашнее задание по всем студентам в рамках курса {"Python"}: '
      f'{student_scores(students_list, "Python")} баллов')


# print(best_student.grades)
# print(best_student.courses_in_progress)
# print(best_lecturer.grades)
# print(cool_mentor)
# print(best_lecturer, 'best_lecturer')
# print(anton_student)
# print(best_student)
# print(igor_lecturer, 'igor_lecturer')
# print(best_lecturer > igor_lecturer)
# print(best_student > anton_student)
