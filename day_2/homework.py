import dataclasses
import random
from typing import List


@dataclasses.dataclass(frozen=True)
class Worker:
    name: str
    surname: str
    phone_number: str


def get_bonuses(workers: List[Worker], bonus_limit):
    if bonus_limit > 0:
        result = {}
        for worker in workers:
            result[worker] = random.randint(0, bonus_limit)
        return result
    else:
        raise Exception


list_of_workers = [
    Worker('Kamil', 'Nowak', '532332445'),
    Worker('Jan', 'Kowalski', '123456789')
]

print(get_bonuses(list_of_workers, bonus_limit=1000))
# Worker(name='Kamil', surname='Nowak', phone_number='532332445'): 1000
# Worker(name='Jan', surname='Kowalski', phone_number='123456789'): 1000