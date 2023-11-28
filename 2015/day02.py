from typing import List

# Day 2: I Was Told There Would Be No Math

test_data = '''2x3x4
1x1x10'''.split('\n')


def part1(data: List[str]):
    s = 0
    for line in data:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        s += 2 * l * w + 2 * w * h + 2 * h * l
        all = [l, w, h]
        low1 = min(all)
        all.remove(low1)
        low2 = min(all)
        s += low1 * low2
    return s


def part2(data: List[str]):
    r = 0
    for line in data:
        l, w, h = line.split('x')
        l, w, h = int(l), int(w), int(h)
        all = [l, w, h]
        low1 = min(all)
        all.remove(low1)
        low2 = min(all)
        r += low1 * 2 + low2 * 2 + l * w * h
    return r


def main():
    with open('inputs/day02.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 58 + 43, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 1588178, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 34 + 14, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 3783758, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
