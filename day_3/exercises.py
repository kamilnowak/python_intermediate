import abc
import re
from dataclasses import dataclass


class Animal(abc.ABC):
    @abc.abstractmethod
    def sound(self):
        pass


class Cat(Animal):
    def sound(self):
        print('Meow!')


class Dog(Animal):
    def sound(self):
        print('Hau!')


class Human:
    def get_name(self):
        return "Human"


class Coder:
    def get_name(self):
        return "Coder"


class PythonDev(Coder, Human):
    pass


python_developer = PythonDev()
print(python_developer.get_name())

from datetime import datetime


@dataclass()
class BaseEvent(abc.ABC):
    created_at: datetime
    created_by: str
    name: str

    @abc.abstractmethod
    def log_event(self):
        pass

    def send_notification(self):
        self.log_event()
        if self.is_important_event():
            print('email sent')

    @abc.abstractmethod
    def is_important_event(self):
        pass


@dataclass()
class UserEvent(BaseEvent):
    email: str

    def log_event(self):
        print(self)

    def is_important_event(self):
        return self.name in ['USER_CREATED', 'USER_DELETED', 'USER_CHANGED']
        # return self.name == 'USER_CREATED' or self.name == 'USER_DELETED'


my_event = UserEvent(
    created_at=datetime.now(),
    created_by='Kamil Nowak',
    name='USER_CREATED',
    email='john@example.com'
)
my_event.send_notification()


def get_long_words(text, min_length):
    return re.findall(r"\w{" + str(min_length) + ",}", text)


print(get_long_words('Ala ma kota', min_length=3))


def get_abbreviation(text: str):
    new_text = text.title()
    regex_result = re.findall(r"[A-ZŻ]", new_text)
    return ''.join(regex_result)

print(get_abbreviation('Software Development Academy'))  # SDA
print(get_abbreviation('SoftwareDevelopmentAcademy'))  # SDA
print(get_abbreviation('Polski Związek Piłki Nożnej'))  # PZPN
print(get_abbreviation('Żywiecki Klub Żużlowy'))  # ŻKŻ
print(get_abbreviation('software development academy'))  # SDA


def replace_name(replace_from, replace_to, text):
    return re.sub(replace_from, replace_to, text, flags=re.IGNORECASE)

print(replace_name("ala", "Ania", "ala ma kota. Ala ma psa"))


def is_valid_number(number):
    return bool(re.findall(r'(\(?\+([1-9][0-9])\)?)?[1-9][0-9]{2}-?[0-9]{3}-?[0-9]{3}', number))

print(is_valid_number('5436d8A56'))  # False
print(is_valid_number('543628356'))  # True
print(is_valid_number('3466'))  # False
print(is_valid_number('000000000'))  # False
print(is_valid_number('+48504123645'))  # True
print(is_valid_number('(+48)504-123-643'))  # True



