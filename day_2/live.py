from collections import namedtuple
from dataclasses import dataclass

NumberInfo = namedtuple('NumberInfo',
                        'number area_code delimiter')
number_namedtouple = NumberInfo('13321444', '+48', '-')
# number_namedtouple.area_code

@dataclass(frozen=False)
class NumberInfoData:
    number: str
    area_code: str
    delimiter: str = '-'

    def call_someone(self):
        self.number = '123'
        print("called president")


number_dataclass = NumberInfoData('13321444', '+48')

print(number_dataclass)
number_dataclass.call_someone()