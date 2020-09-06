#
# print(my_func(value=10))  # [10]
# print(my_func(value=20))  # [20]
# print(my_func(value=20, my_list=[30]))  # [30, 20]
import typing
from textwrap import wrap


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
