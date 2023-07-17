from typing import Callable
from pprint import pprint

def inner_scrub(path: list[str], data: any, generator: Callable[[], str]):
    this = data
    for idx, x in enumerate(path):
        pprint(this)
        if idx == len(path) - 1:
            this[x] = generator()
        if x.endswith('[]'):
            for y in this[x[:-2]]:
                inner_scrub(path[idx+1:], y, generator)
            continue
        if not x in this:
            raise KeyError(x)
        this = this[x]
            


def scrub(path: str, data: any, generator: Callable[[], str]) -> any:
    split_path = path.split('.')
    inner_scrub(split_path, data, generator)
    return data