from typing import List

# Day 18: Like a GIF For Your Yard

test_data = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''.split('\n')

PART2_FLAG = False


def get_coord(data, coord):
    x, y = coord
    if x < 0 or y < 0 or x >= len(data[0]) or y >= len(data):
        return '.'
    elif PART2_FLAG and coord in [(0, 0), (0, len(data) - 1), (len(data[0]) - 1, 0), (len(data[0]) - 1, len(data) - 1)]:
        return '#'
    return data[y][x]


def get_neighbors(data, coord):
    neighbors = []
    x, y = coord
    for a in range(-1, 2, 1):
        for b in range(-1, 2, 1):
            if a == b == 0:
                continue
            neighbors.append(get_coord(data, (x + b, y + a)))
    return neighbors


def part1(data: List[str], steps):
    # Prepare two grids and alternate between them
    grids = [[list(line) for line in data], [list(line) for line in data]]
    if PART2_FLAG:
        grids[0][0][0] = '#'
        grids[0][0][-1] = '#'
        grids[0][-1][0] = '#'
        grids[0][-1][-1] = '#'
        grids[1][0][0] = '#'
        grids[1][0][-1] = '#'
        grids[1][-1][0] = '#'
        grids[1][-1][-1] = '#'
    # print('grids:', grids)
    h, w = len(data), len(data[0])
    for i in range(steps):
        current_gen = grids[i % 2]
        next_gen = grids[(i + 1) % 2]

        # Debug
        #for row in current_gen:
        #    print(''.join(row))
        #input(f'i = {i}')

        for y in range(h):
            for x in range(w):
                alive = (current_gen[y][x] == '#')
                alive_neighbors = sum(1 for n in get_neighbors(current_gen, (x, y)) if n == '#')
                cell_next = '#' if alive_neighbors == 3 or (alive and alive_neighbors == 2) else '.'
                if PART2_FLAG and (x, y) in [(0, 0), (0, h - 1), (w - 1, 0), (w - 1, h - 1)]:
                    cell_next = '#'
                next_gen[y][x] = cell_next

    alive_count = 0
    for line in grids[steps % 2]:
        alive_count += sum([1 for c in line if c == '#'])
    return alive_count


def part2(data: List[str], steps):
    global PART2_FLAG
    PART2_FLAG = True
    return part1(data, steps)


def main():
    with open('inputs/day18.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 4)
    assert part1_test_result == 4, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data, 100)
    assert part1_result == 821, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data, 5)
    assert part2_test_result == 17, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data, 100)
    assert part2_result == 886, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
