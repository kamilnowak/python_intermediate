

class Student:
    def __init__(self, name: str, surname: str, age: int, grades=None):
        if grades is None:
            grades = []
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = grades

    def __repr__(self):
        return f'{self.name} {self.surname} - {self.age} years old'

    # def __str__(self):
    #     return f'{self.name} {self.surname}'

    def add_grades(self, *grades):
        for grade in grades:
            if 1 <= grade <= 6:
                self.grades.append(grade)
            else:
                raise ValueError(f"Grade {grade} is out of range 1-6")

    def remove_grade(self, idx: int):
        try:
            return self.grades.pop(idx)
        except IndexError:
            raise IndexError("Can't delete index - out of range")

#
# student = Student("Jan", "Kowalski", 20)
# student.add_grades(5, 5, 2)  # grades = [5, 5, 2]
# student.remove_grade(1)
# print(student.grades)
# student.add_grades(10)


class School:
    def __init__(self, university_name: str, address: str):
        self.university_name = university_name
        self.address = address
        self.students = []

    def add_student(self, new_student: Student):
        if type(new_student) is Student:
            self.students.append(new_student)
        else:
            raise TypeError

    def add_students(self, *students: Student):
        are_all_object_students = all(type(stud) is Student for stud in students)
        if not are_all_object_students:
            raise TypeError
        for stud in students:
            self.add_student(stud)



