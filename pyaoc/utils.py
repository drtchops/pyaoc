from dataclasses import dataclass
from math import sqrt
from typing import Self


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0

    def __add__(self, other: Point) -> Self:
        return self.__class__(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Point) -> Self:
        return self.__class__(self.x - other.x, self.y - other.y)

    def distance(self, other: Point) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

    def as_tuple(self) -> tuple[int, int]:
        return (self.x, self.y)


@dataclass(frozen=True)
class Point3D:
    x: int = 0
    y: int = 0
    z: int = 0

    def __add__(self, other: Point3D) -> Self:
        return self.__class__(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Point3D) -> Self:
        return self.__class__(self.x - other.x, self.y - other.y, self.z - other.z)

    def distance(self, other: Point3D) -> float:
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def as_tuple(self) -> tuple[int, int, int]:
        return (self.x, self.y, self.z)


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
