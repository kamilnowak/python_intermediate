from collections import namedtuple
from dataclasses import dataclass, field
from typing import List

my_data = [
    {
       "name": "Jan",
       "Surname": "Kowalski",
    },
    {
       "name": "Artur",
       "Surname": "Nowak",
    },
]

Person = namedtuple('Person', 'name surname')


def labeled_entries(data: List) -> List[Person]:
    return [Person(entry['name'], entry['Surname']) for entry in data]


@dataclass()
class Student:
    name: str
    surname: str
    age: int
    grades: List = field(default_factory=list)

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


@dataclass()
class School:
    university_name: str
    address: str
    students: List = field(default_factory=list)

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


@dataclass(order=True)
class Country:
    name: str = field(compare=False)
    population: int
    area: float
    coastline: float


my_countries = [
    Country('Poland', 2000, 5000.24, 800.5),
    Country('Germany', 3000, 5000.24, 800.5),
    Country('Russia', 1000, 5000.24, 800.5),
]

print(sorted(my_countries, key=lambda x: x.population))
