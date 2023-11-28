from typing import List
import utils

# Day 4: The Ideal Stocking Stuffer

test_data = '''abcdef'''.split('\n')


def search_prefix(s: str, n: int) -> int:
    i = 1
    prefix = '0' * n
    while True:
        result = utils.md5(s + str(i))
        if result.startswith(prefix):
            return i
        i += 1


def part1(data: List[str]):
    return search_prefix(data[0], 5)


def part2(data: List[str]):
    return search_prefix(data[0], 6)


def main():
    with open('inputs/day04.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 609043, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 254575, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 1038736, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
