#
# print(my_func(value=10))  # [10]
# print(my_func(value=20))  # [20]
# print(my_func(value=20, my_list=[30]))  # [30, 20]
import typing
from dataclasses import dataclass
from math import pi
from textwrap import wrap
import abc

def format_phone_number(number, area_code='+48', delimiter=' '):
    wrapped_number = delimiter.join(wrap(number, 3))
    # return delimiter.join([area_code, number[0:3], number[3:6], number[6:9]])
    return area_code + delimiter + wrapped_number

# format_phone_number(number='697123754')
# # '+44 697 123 754'
#
# format_phone_number('697123754', delimiter=' ')
# # '+48 697 123 754'
#
# format_phone_number('697123754', '+44', '-')
# # '+48 697 123 754'


def my_sum(*args):
    result = 0
    for arg in args:
        result += arg
    return result

# print(my_sum(1, 5, 6))  # 6


def my_sum_kwargs(**kwargs):
    # wartosci od uzytkownika  ['697120906']
    # dodajemy do listy area_code  ['697120906', '+48']

    print(kwargs)
    result = 0
    for arg in kwargs.values():
        result += arg
    return result

# my_sum_kwargs(1, 5, 6)  # 6
# print(my_sum_kwargs(eggs=3, spam=4, cheese=7))  # 6


positional_data = ['697120906', '+44', ' ']

# print(format_phone_number(number=['697120906', '+44', ' ']))  # positional_data
# print(format_phone_number('697120906', '+44', ' '))  # *positional_data

keyword_data = {
    'area_code': '+44',
    'number': '606323135',
    'delimiter': ' '
}
# print(keyword_data) # {'area_code': '+44','number': '606323135','delimiter': ' '}
# print(*keyword_data) # ['area_code', 'number', 'delimiter']
# print(**keyword_data)  # number=X, area_code=
# print(format_phone_number(*keyword_data))


def my_func(value, my_list=None):
    if my_list is None:
        my_list = []
    print(hex(id(my_list)))
    my_list.append(value)
    return my_list


# print(my_func(1), )
# print(my_func(3))
# print(my_func(5))


def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = ''.join(
            f' {attr}="{value}"'
            for attr, value in sorted(attrs.items())
        )
    else:
        attr_str = ''

    if content:
        # <div style=X class=Y>content</div>
        return '\n'.join(f'<{name}{attr_str}>'
                         f'{c}'
                         f'</{name}>' for c in content)
    else:
        return f'<{name}{attr_str}/>'


# print(tag('br'))
# print(tag('p', 'hello'))
# print(tag('p', 'hello', 'world'))
# print(tag('p', 'hello', id=33))
# print(tag('p', 'hello', 'world', cls='sidebar'))
# print(tag(content='testing', name='img'))
# my_dict = {
#     'name': 'img',
#     'title': 'Sunset',
#     'img': 'sunset.jpg',
#     'cls': 'framed'
# }
# print(tag(**my_dict))

# numbers_info = ('68321323', '+48', '-')
# number, area_code, delimiter = numbers_info
# number, *others = numbers_info

# print(type(numbers_info))
# print(type(number))
# print(type(others))

a = 1
b = 5
print(a)
print(b)
# a, b = b, a

# print(a)
# print(b)


numbers_info = ('68321323', '+48', '-', '123', 'test')
# number, area_code, delimiter = numbers_info
# number, *others = numbers_info
others, *delimiter = numbers_info
# print(others)


def is_isogram(word: str) -> bool:
    return len(word) == len(set(word))


print(is_isogram('test'))
# print(is_isogram(123))



my_dict = {
    'name': 'img',
    'title': 'Sunset',
    'img': 'sunset.jpg',
    'cls': 'framed'
}


class MyOwnException(Exception):
    pass


def foo():
    try:
        print(my_dict['not_exists'])
    except (ValueError, KeyError):
        return
    else:
        print('Else')
    finally:
        print('Finally')

# foo()

# class Person(object):


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old.'

    def check_finance(self):
        return self.show_salary()


class Worker(Person):
    def __init__(self, name, age, rate, number_of_hours):
        Person.__init__(self, name, age)
        self.rate = rate
        self.number_of_hours = number_of_hours

    def show_salary(self):
        return self.rate * self.number_of_hours


class Student(Person):
    def __init__(self, name, age, scholarship):
        Person.__init__(self, name, age)
        self.scholarship = scholarship

    def show_salary(self):
        return self.scholarship

    @classmethod
    def create_from_string(cls, string: str):
        name, age, scholarship = string.split()
        age, scholarship = int(age), float(scholarship)
        if cls.is_correct_name(name):
            return cls(name, age, scholarship)

    @staticmethod
    def is_correct_name(name: str):
        if name[0].isupper() and len(name) > 3:
            return True
        return False

# p3 = Student("Agata", 22, 1000)
# print(p3.show_salary())
student2 = Student.create_from_string("Maciej 21 600")
print(Student.is_correct_name('Ka'))

print(student2)
# print(Student.is_correct_name('Ka'))

#
# class WorkingStudent(Worker, Student):
#     def __init__(self, name, age, rate, number_of_hours, scholarship):
#         Worker.__init__(self, name, age, rate, number_of_hours)
#         Student.__init__(self, name, age, scholarship)
#
#     def show_salary(self):
#         return self.rate * self.number_of_hours + self.scholarship
#
# p1 = Person("Henryk", 54)
# # p2 = Worker("Jacek", 26, 20, 160)
# p2 = Worker(name="Jacek", age=26, rate=20, number_of_hours=160)
# # p3 = Student("Agata", 22, 1000)
# p4 = WorkingStudent(name="Monika", age=24, rate=9.5,
#                     number_of_hours=70, scholarship=500)
#
# print(p1)
# print(p2)
# print(p3)
# print(p4.check_finance())
#
#
# # class Figura(abc.ABC):
class Figura:
    @abc.abstractmethod
    def obwod(self):
        pass
    @abc.abstractmethod
    def pole(self):
        pass

# class Prostokat(Figura):
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#     def obwod(self):
#         return 2 * (self.a + self.b)
#     def pole(self):
#         return self.a * self.b
#
# from math import pi
#
# class Kolo(Figura):
#     def __init__(self, r):
#         self.r = r
#     def obwod(self):
#         return 2 * self.r * pi
#     # def pole(self):
#     #     return pi * self.r ** 2
#
# prostokat = Prostokat(3 ,5)
# kolo = Kolo(12)
# print(prostokat.obwod())
# print(kolo.obwod())
# print(kolo.pole())
# # figura = Figura()
#
#
@dataclass
class Prostokat(Figura):
    a: int
    b: int

    def obwod(self):
        return 2 * (self.a + self.b)

    def pole(self):
        return self.a * self.b

prostokat = Prostokat(3 ,5)
# kolo = Kolo(12)
print(str(prostokat))
print(prostokat.obwod())