from typing import List, Dict
import utils

# Day 7: Some Assembly Required

test_data = '''123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> a
NOT x -> h
NOT y -> i'''.split('\n')


def solve(data: List[str], register: Dict):
    while True:
        for i in range(len(data)):
            instr = data[i]
            left_side, to_var = instr.split(' -> ')
            if to_var in register:
                continue
            v1, v2 = None, None
            keyword = None
            for k in [' AND ', ' OR ', ' LSHIFT ', ' RSHIFT ']:
                if k in left_side:
                    v1, v2 = left_side.split(k)
                    keyword = k
                    break
            if 'NOT ' in left_side:
                v1 = left_side.replace('NOT ', '')
                keyword = 'NOT '
            elif keyword is None:
                keyword = ' (EQ) '
                v1 = left_side

            # print('keyword:', keyword, 'v1:', v1, 'v2:', v2, 'register:', register)
            # input()

            if (v1.isdigit() or v1 in register) and (v2 is None or v2.isdigit() or v2 in register):
                v1 = int(v1) if v1.isdigit() else register[v1]
                if v2 is not None:
                    v2 = int(v2) if v2.isdigit() else register[v2]

                if keyword == ' AND ':
                    value = v1 & v2
                elif keyword == ' OR ':
                    value = v1 | v2
                elif keyword == ' LSHIFT ':
                    value = v1 << v2
                elif keyword == ' RSHIFT ':
                    value = v1 >> v2
                elif keyword == 'NOT ':
                    value = utils.bit_not(v1, numbits=16)
                else:
                    value = v1

                # Use mask to cut off higher bits
                value = value & 65535

                # print('Setting register:', keyword, v1, v2, '=>', to_var, '=', value)
                # input()

                if to_var == 'a':
                    return value
                register[to_var] = value


def part1(data: List[str]):
    return solve(data, {})


def part2(data: List[str]):
    return solve(data, {'b': 46065})


def main():
    with open('inputs/day07.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 114, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 46065, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 14134, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
