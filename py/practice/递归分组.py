from enum import Enum
from typing import Iterator, Final
from pprint import pprint

class sex(Enum):
    male = "male"
    famale = "famale"

    def __repr__(self):
        return repr(self.value)

data :Final[dict[str, any]] = [
    {"id": 1, "sex": sex.male, "name": "Tom"}, 
    {"id": 2, "sex": sex.famale, "name": "Amy"}, 
    {"id": 3, "sex": sex.male, "name": "Tony"}, 
    {"id": 4, "sex": sex.male, "name": "Bob"}, 
    {"id": 5, "sex": sex.famale, "name": "Lisa"}
]

def group_by_sex(d: Iterator[dict[str, any]], o:dict[sex, list[dict[str, any]]]=None):
    if o is None:
        o = dict()
    try:
        i = next(d)
        if o.get(i.get('sex')): o.get(i.get('sex')).append(i)
        else: o.setdefault(i.get('sex'), [i])
    except StopIteration:
        return o
    return group_by_sex(d, o)

pprint(group_by_sex(iter(data)))
