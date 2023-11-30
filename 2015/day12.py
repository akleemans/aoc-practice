from typing import List
import json

# Day 12: JSAbacusFramework.io

test_data = '''[1,2,3]
{"a":{"b":4,"c":"red"},"c":-1}
[-1,{"a":1}]'''.split('\n')


def part1(data: List[str]):
    numbers = []
    numerals = '-1234567890'
    for line in data:
        in_string = False
        current_nr = ''
        for c in line:
            if c == '"':
                in_string = not in_string
                continue
            if not in_string:
                if c in numerals:
                    current_nr += c
                elif current_nr != '':
                    numbers.append(int(current_nr))
                    current_nr = ''
    return sum(numbers)


def walk(node) -> int:
    if isinstance(node, int):
        return node
    elif isinstance(node, str):
        return 0
    elif isinstance(node, list):
        return sum([walk(c) for c in node])
    elif isinstance(node, dict):
        if 'red' in [c for c in node.values() if isinstance(c, str)]:
            return 0
        return sum([walk(c) for c in node.values()])


def part2(data: List[str]):
    s = 0
    for line in data:
        parsed = json.loads(line)
        s += walk(parsed)
    return s


def main():
    with open('inputs/day12.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 9, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 111754, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 5, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 65402, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
