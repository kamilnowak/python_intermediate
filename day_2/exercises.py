from collections import namedtuple
from typing import List

my_data = [
    {
       "name": "Jan",
       "Surname": "Kowalski",
    },
    {
       "name": "Artur",
       "Surname": "Nowak",
    },
]

Person = namedtuple('Person', 'name surname')


def labeled_entries(data: List) -> List[Person]:
    return [Person(entry['name'], entry['Surname']) for entry in data]


print(labeled_entries(my_data)[0].)

