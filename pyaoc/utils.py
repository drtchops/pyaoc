from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, other: "Point") -> Self:
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: "Point") -> Self:
        return self.__class__(self.x - other.x, self.y - other.y)


def gcd(a: int, b: int) -> int:
    while b != 0:
        t = b
        b = a % b
        a = t
    return a


def lcm(a: int, b: int, *integers: int) -> int:
    result = int(a * b / gcd(a, b))
    for i in range(len(integers)):
        result = lcm(result, integers[i])
    return result
