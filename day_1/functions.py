from textwrap import wrap
from typing import Union, List, Tuple


def format_phone_number(number: str, area_code: str = '+48', delimeter: str = '-') -> str:
    wrapped_number = delimeter.join(wrap(number, 3))
    return f"{area_code} (0) {wrapped_number}"


def less_than(cutoff_val: int, values: List[int]) -> Tuple[List[int], bool]:
    # iterujemy po liscie values
    # sprawdzamy czy wartosc jest mniejsza od cutoff
    # jezeli tak: dodaj do listy
    # jezeli nie: nie dodawaj, ustaw flage na True
    result = []
    was_something_remove = False
    for value in values:
        if value < cutoff_val:
            result.append(value)
        else:
            was_something_remove = True
    return result, was_something_remove


def is_palindrom(text: str) -> bool:
    # funkcja powinna zwrócić wartość True jeśli zdanie jest palindrom i False jeśli nie.
    text = text.lower().replace(',', '').strip()
    return text == text[::-1]


def remove_duplicates(values):
    # funkcja powinna zwrócić listę bez duplikatów oraz informację czy był jakiś duplikat
    pass


def safe_division(number: int, divisor: int, ignore_zero_division: bool = False) -> Union[float, int]:
    # funkcja na podstawie flagi ignore_zero_division powinno zwrócić float('inf') lub wyjątek
    # ignore_zero_division powinno domyślnie być False
    try:
        return number / divisor
    except ZeroDivisionError:
        if ignore_zero_division:
            return float('inf')
        raise


