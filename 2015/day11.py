from typing import List

# Day 11: Corporate Policy

test_data = '''abcdefgh'''.split('\n')


def next_pw(pw: str) -> str:
    pw = list(pw)
    for i in range(len(pw) - 1, 0, -1):
        if pw[i] == 'z':
            pw[i] = 'a'
        else:
            pw[i] = chr(ord(pw[i]) + 1)
            break
    return ''.join(pw)


def is_valid(pw: str) -> bool:
    if 'i' in pw or 'o' in pw or 'l' in pw:
        return False

    increasing = False
    for i in range(len(pw) - 2):
        a, b, c = pw[i], pw[i + 1], pw[i + 2]
        if ord(a) == ord(b) - 1 == ord(c) - 2:
            increasing = True
            break
    if not increasing:
        return False

    pairs = set()
    for i in range(len(pw) - 1):
        a, b = pw[i], pw[i + 1]
        if a == b:
            pairs.add(a + a)

    return len(pairs) >= 2


def part1(data: List[str]):
    pw = data[0]
    while not is_valid(pw):
        pw = next_pw(pw)
    return pw


def part2(data: List[str]):
    pw = data[0]
    pw = next_pw(pw)
    while not is_valid(pw):
        pw = next_pw(pw)
    return pw


def main():
    with open('inputs/day11.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 'abcdffaa', f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 'vzbxxyzz', f'Part 1 returned {part1_result}'

    part2_result = part2([part1_result])
    assert part2_result == 'vzcaabcc', f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
