from typing import List

# Day 6: Probably a Fire Hazard

test_data = '''turn on 0,0 through 999,999
toggle 0,0 through 999,0
turn off 499,499 through 500,500'''.split('\n')


def part1(data: List[str]):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for instr in data:
        parts = instr.split(' ')
        x0, y0 = parts[-3].split(',')
        x1, y1 = parts[-1].split(',')
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if 'turn off' in instr:
                    grid[y][x] = 0
                elif 'turn on' in instr:
                    grid[y][x] = 1
                elif 'toggle' in instr:
                    grid[y][x] = 0 if grid[y][x] == 1 else 1
    return sum([sum(line) for line in grid])


def part2(data: List[str]):
    grid = [[0 for _ in range(1000)] for _ in range(1000)]
    for instr in data:
        parts = instr.split(' ')
        x0, y0 = parts[-3].split(',')
        x1, y1 = parts[-1].split(',')
        x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
        for x in range(x0, x1 + 1):
            for y in range(y0, y1 + 1):
                if 'turn off' in instr:
                    grid[y][x] = max(grid[y][x] - 1, 0)
                elif 'turn on' in instr:
                    grid[y][x] = grid[y][x] + 1
                elif 'toggle' in instr:
                    grid[y][x] = grid[y][x] + 2
    return sum([sum(line) for line in grid])


def main():
    with open('inputs/day06.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 10 ** 6 - 1000 - 4, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 400410, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 1001996, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 15343601, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
