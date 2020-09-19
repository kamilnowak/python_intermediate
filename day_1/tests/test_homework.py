import unittest

#
# class StudentTestCase(unittest.TestCase):
#     def
import pytest

from day_1.homework import Student, School


def test_student():
    stud = Student("Jan", "Kowalski", 20)
    assert stud.grades == []


@pytest.mark.parametrize("grades_input, expected", [
    ([2, 5], [2, 5]),
    ([2, 6], [2, 6]),
    ([1, 5], [1, 5]),
])
def test_add_grades(grades_input, expected):
    stud = Student("Jan", "Kowalski", 20)
    stud.add_grades(*grades_input)
    assert stud.grades == expected

def test_remove_grade_out_of_list():
    stud = Student("Jan", "Kowalski", 20)
    stud.add_grades(3, 5)  # grades = [3, 5]
    with pytest.raises(IndexError) as exc:
        stud.remove_grade(7)
    assert str(exc.value) == "Can't delete index - out of range"

def test_remove_grade_within_list():
    stud = Student("Jan", "Kowalski", 20)
    stud.add_grades(3, 5)  # grades = [3, 5]
    stud.remove_grade(1)
    assert stud.grades == [3]

@pytest.mark.parametrize("entry, expected", [
    (Student("Jan", "Kowalski", 20), 1),
    (Student("Jan", "Nowak", 22), 1),
])
def test_school_add_student(entry, expected):
    school = School("SDA", "Warszawa, Pańska 12")
    school.add_student(entry)
    print(str(school.students[0]))
    print(school.students)
    assert len(school.students) == expected


@pytest.mark.parametrize("entry, expected", [
    ([Student("Jan", "Kowalski", 20), Student("Adam", "Nowak", 21)], 2),
    ([Student("Jan", "Kowalski", 20)], 1),
])
def test_school_add_students(entry, expected):
    school = School("SDA", "Warszawa, Pańska 12")
    school.add_students(*entry)
    assert len(school.students) == expected


@pytest.mark.parametrize("entry, expected", [
    ([Student("Jan", "Kowalski", 20), "Not Student 2"], 0),
    (["Not Student 1"], 0),
])
def test_school_add_students_not_student_type(entry, expected):
    school = School("SDA", "Warszawa, Pańska 12")
    with pytest.raises(TypeError):
        school.add_students(*entry)
    assert len(school.students) == expected
