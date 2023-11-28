from typing import List

# Day 1: Not Quite Lisp

test_data = '''))((((('''.split('\n')


def part1(data: List[str]):
    data = data[0]
    return data.count('(') - data.count(')')


def part2(data: List[str]):
    data = data[0]
    floor = 0
    for pos in range(len(data)):
        # print('At pos', pos, 'char:', data[pos])
        if data[pos] == ')':
            floor -= 1
        else:
            floor += 1
        if floor == -1:
            return pos + 1


def main():
    with open('inputs/day01.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 3, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 138, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 1, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 1771, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
