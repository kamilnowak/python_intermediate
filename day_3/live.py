import abc
import typing
from heapq import heappush
from heapq import heappop


def heapsort(iterable):
    h = []
    for value in iterable:
        heappush(h, value)
        print(h)
    result = [heappop(h) for i in range(len(h))]
    print(f'at the end: {h}')
    return result


# class A:
# ...     pass
# ...
# >>>
# class B:
# ...     pass
# ...
# >>>
# class C(B,A):
# ...     pass
# ...
# a = A()
# isinstance(a, A)
# True
# type(a) == A
# True
# >>>
# >>>
# isinstance(a, B)
# False
# >>>
# c = C()
# type(c)
# <class '__main__.C'>
# isinstance(c, C)
# True
# isinstance(c, B)
# True
# type(c) == C
# True
# issubclass(C, A)
# True
# issubclass(A, C)
# False
# issubclass(A, B)
# False
# issubclass(C, B)


# try:
# ...     result = user.surname
# ... except AttributeError:
# ...     print('error')

# has_surname = hasattr(user, 'surname')
# if has_surname:
#     pass
# else:
#     print('no surname')

# getattr(user, 'surname', 'no surname')


class MusicalInstrument(abc.ABC):
    def __init__(self, price):
        self.price = price

    # @abc.abstractmethod
    def play(self):
        pass

    def play_loud(self):
        self.play()


class Guitar(MusicalInstrument):
    def __init__(self, price, number_of_strings):
        super().__init__(price)
        self.number_of_strings = number_of_strings

    def play(self):
        print('Brzdęk')


class Piano(MusicalInstrument):
    def play(self):
        print('Ding')


class Violin(MusicalInstrument):
    def play(self):
        print('Skrzyp Skrzyp')

def orchest(instruments: typing.List[MusicalInstrument]):
    for instrument in instruments:
        if isinstance(instrument, MusicalInstrument):
            instrument.play()
        # else:
        #     print('not an instrument')


guitar = Guitar(price=200, number_of_strings=5)
piano = Piano(1000)
violin = Violin(500)

orchest([guitar, piano, violin, 5])




# REGEX
import re
re.sub(r'\w{4}', 'psa', 'Ala ma kota')
# 'Ala ma psa'

re.subn(r' \w{4}', 'psa', 'Ala ma kota')
# ('Ala mapsa', 1)

it = re.finditer(r'.la', 'ola ala ela')
for match in it:
    print(match)
# <re.Match object; span=(0, 3), match='ola'>
# <re.Match object; span=(4, 7), match='ala'>
# <re.Match object; span=(8, 11), match='ela'>


re.search(r'ala', 'ala ola')
# <re.Match object; span=(0, 3), match='ala'>

re.findall(r'ala', 'ala ola')
# ['ala']

re.match(r'\w+', 'test')
# <re.Match object; span=(0, 4), match='test'>
re.fullmatch(r'\w+', 'te st') # brak wyniku ze względu na to że całe zdanie "te st" nie spełnia wyrażenia regularnego



re.split(r'[A-Z]', 'AlaMaKota')
# ['', 'la', 'a', 'ota']

re.split(r'(?=[A-Z])', 'AlaMaKota')
# ['', 'Ala', 'Ma', 'Kota']