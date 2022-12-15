"""Student class and object creating program."""


class Student:
    """Student class."""

    def __init__(self, name):
        """Student class construct.
        Creates student type object

        Parameters:
            name(str):Name of student.
            """
        self.name = name
        self.finished = False


student1 = Student("John")
print(student1)
print(student1.name)
print(student1.finished)

student2 = Student("Adam")
print(student2)
print(student2.name)
print(student2.finished)
