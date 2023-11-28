from typing import List
from utils import Coord

# Day 3: Perfectly Spherical Houses in a Vacuum

test_data = '''^>v<'''.split('\n')


def part1(data: List[str]):
    visits = []
    coord = Coord(0, 0)
    visits.append(coord.pair())
    for d in data[0]:
        if d == '>':
            coord.x += 1
        elif d == '<':
            coord.x -= 1
        elif d == '^':
            coord.y -= 1
        elif d == 'v':
            coord.y += 1
        visits.append(coord.pair())
    return len(set(visits))


def part2(data: List[str]):
    visits = []
    coord1 = Coord(0, 0)
    coord2 = Coord(0, 0)
    visits.append(coord1.pair())
    for i in range(len(data[0])):
        d = data[0][i]
        coord = [coord1, coord2][i % 2]
        if d == '>':
            coord.x += 1
        elif d == '<':
            coord.x -= 1
        elif d == '^':
            coord.y -= 1
        elif d == 'v':
            coord.y += 1
        visits.append(coord.pair())
    return len(set(visits))


def main():
    with open('inputs/day03.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 4, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 2572, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 3, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2631, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
