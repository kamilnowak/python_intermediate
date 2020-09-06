import pytest

from day_1.functions import format_phone_number
from day_1.functions import less_than
from day_1.functions import remove_duplicates
from day_1.functions import is_palindrom
from day_1.functions import safe_division


def test_format_number():
    data = {
        'delimeter': '/',
        'number': '697120906',
        'area_code': '+49',
    }
    assert format_phone_number(**data) == '+49 (0) 697/120/906'

    data_list = ['697120906', '+49']
    assert format_phone_number(*data_list) == '+49 (0) 697-120-906'


@pytest.mark.parametrize("input,expected", [
    ({
        'number': '697120906'
     }, '+48 (0) 697-120-906'),
    ({
        'number': '697120906',
        'area_code': '+49'
     }, '+49 (0) 697-120-906'),
])
def test_format_number_advanced(input, expected):
    assert format_phone_number(**input) == expected


def test_less_than():
    # TODO #3 popraw test ;)
    data = {
        'cutoff_val': 5,
        'values': [1, 2, 8]
    }
    assert less_than(**data) == ([1, 2], True)


@pytest.mark.parametrize("test_input,expected", [
    ('ala', True),
    ('igor łamał rogi', True),
    ('igor łamał rogi  ', True),
    ('igor łamAł Rogi  ', True),
    ('igor łamAł Rogi  ,', True),
    ('Ala ma kota', False),
])
def test_is_palindrom(test_input, expected):
    assert is_palindrom(test_input) == expected


def test_remove_duplicates():
    list_without_duplicates = remove_duplicates(['Jan', 'Magda', 'Monika', 'Magda'])
    assert list_without_duplicates == (['Jan', 'Magda', 'Monika'], True)


def test_safe_division():
    assert safe_division(10, 2) == 5.0
    assert safe_division(10, 0, ignore_zero_division=True) == float('inf')
    with pytest.raises(ZeroDivisionError):
        safe_division(10, 0)
