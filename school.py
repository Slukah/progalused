import random


class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.courses = []

    def add_student(self, student):
        if student not in self.students:
            id = random.randint(1, 100)
            while any([school_student.get_id() == id for school_student in self.students]):
                id = random.randint(1, 100)
            student.set_id(id)
            self.students.append(student)

    def get_students(self):
        return self.students

    def add_course(self, course):
        if course not in self.courses:
            self.courses.append(course)

    def get_courses(self):
        return self.courses

    def add_student_grade(self, student, course, grade):
        if student in self.students and course in self.courses:
            student.add_grade(tuple([course, grade]))
            course.add_grade(tuple([student, grade]))
