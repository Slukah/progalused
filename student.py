"""Student class and object creating program."""


class Student:
    """Student class."""

    def __init__(self, name):

        self.name = name
        self.grades = []
        self.id = None

    def get_id(self):
        return self.id

    def set_id(self, id):
        if self.id == None:
            self.id = id

    def __repr__(self):
        return self.name

    def add_grade(self, grade):
        self.grades.append(grade)

    def get_grades(self):
        return self.grades

    def get_average_grade(self):
        total_grade = 0
        for grade in self.grades:
            total_grade += grade[1]
        average_grade = total_grade / len(self.grades)
        return average_grade

