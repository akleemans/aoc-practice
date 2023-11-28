import hashlib
from typing import Tuple


class Coord:
    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y

    def pair(self) -> Tuple[int, int]:
        return self.x, self.y

    def add(self, other: 'Coord'):
        return Coord(self.x + other.x, self.y + other.y)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if other is None:
            return False
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return (self.x, self.y).__hash__()


def md5(s: str) -> str:
    """Hashes a string to md5 and returns the hexadecimal string"""
    return hashlib.md5(s.encode()).hexdigest()


def bit_not(n, numbits=8):
    """Returns bitwise not for a number of bits"""
    return (1 << numbits) - 1 - n
