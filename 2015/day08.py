from typing import List

# Day 8: Matchsticks

test_data = '''""
"abc"
"aaa\\"aaa"
"\\x27"'''.split('\n')


def part1(data: List[str]):
    count = 0
    for line in data:
        decoded = line.encode('ascii', 'backslashreplace').decode('unicode-escape')[1:-1]
        count += len(line) - len(decoded)
    return count


def part2(data: List[str]):
    count = 0
    for line in data:
        # Just count all the ", \ and "" around the string
        count += line.count('"') + line.count('\\') + 2
    return count


def main():
    with open('inputs/day08.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 12, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 1342, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 19, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 2074, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
