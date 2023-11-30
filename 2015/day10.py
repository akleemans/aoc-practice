from typing import List

# Day 10: Elves Look, Elves Say

test_data = ''''''.split('\n')


def solve(data, times: int):
    seq = data[0]
    new_seq = ''
    for n in range(times):
        i = 0
        while i < len(seq):
            current = seq[i]
            count = 0
            while (i + count) < len(seq) and seq[i + count] == current:
                count += 1
            new_seq += str(count) + seq[i]
            i += count

        seq = new_seq
        new_seq = ''
    return len(seq)


def part1(data: List[str]):
    return solve(data, 40)


def part2(data: List[str]):
    return solve(data, 50)


def main():
    with open('inputs/day10.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_result = part1(data)
    assert part1_result == 252594, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 3579328, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
