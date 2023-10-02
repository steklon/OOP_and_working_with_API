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
            sum_ = sum(self.grades[course])
            quantity = len(self.grades[course])
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


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python', 'JavaScript']
best_student.finished_courses += ['Введение в программирование']

anton_student = Student('Антон', 'Антонов', 'man')
anton_student.courses_in_progress += ['Python', 'JavaScript']
anton_student.finished_courses += ['Введение в программирование']

cool_mentor = Reviewer('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

best_lecturer = Lecturer('Иван', 'Иванов')
best_lecturer.courses_attached += ['JavaScript']

igor_lecturer = Lecturer('Игорь', 'Михайлович')
igor_lecturer.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 4)
cool_mentor.rate_hw(best_student, 'Python', 6)
cool_mentor.rate_hw(best_student, 'Python', 9)

cool_mentor.rate_hw(anton_student, 'Python', 5)
cool_mentor.rate_hw(anton_student, 'Python', 1)
cool_mentor.rate_hw(anton_student, 'Python', 5)

best_student.rate_lecturer(best_lecturer, 'JavaScript', 10)
best_student.rate_lecturer(best_lecturer, 'JavaScript', 6)
best_student.rate_lecturer(best_lecturer, 'JavaScript', 1)

anton_student.rate_lecturer(best_lecturer, 'JavaScript', 9)
anton_student.rate_lecturer(best_lecturer, 'JavaScript', 6)
anton_student.rate_lecturer(best_lecturer, 'JavaScript', 5)

best_student.rate_lecturer(igor_lecturer, 'Python', 8)
best_student.rate_lecturer(igor_lecturer, 'Python', 4)
best_student.rate_lecturer(igor_lecturer, 'Python', 6)

anton_student.rate_lecturer(igor_lecturer, 'Python', 1)
anton_student.rate_lecturer(igor_lecturer, 'Python', 4)
anton_student.rate_lecturer(igor_lecturer, 'Python', 5)

# print(best_student.grades)
# print(best_student.courses_in_progress)
# print(best_lecturer.grades)
# print(cool_mentor)
print(best_lecturer, 'best_lecturer')
# print(anton_student)
# print(best_student)
print(igor_lecturer, 'igor_lecturer')
print(best_lecturer > igor_lecturer)
# print(best_student > anton_student)
