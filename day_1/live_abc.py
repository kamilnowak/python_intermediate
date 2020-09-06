import abc
from math import pi


class Figura(abc.ABC):
    @abc.abstractmethod
    def obwod(self):
        pass
    @abc.abstractmethod
    def pole(self):
        pass

class Prostokat(Figura):
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obwod(self):
        return 2 * (self.a + self.b)
    def pole(self):
        return self.a * self.b


class Kolo(Figura):
    def __init__(self, r):
        self.r = r
    def obwod(self):
        return 2 * self.r * pi
    # def pole(self):
    #     return pi * self.r ** 2

prostokat = Prostokat(3 ,5)
kolo = Kolo(12)
print(prostokat.obwod())
print(kolo.obwod())
print(kolo.pole())
# figura = Figura()