from typing import List

# Day 17: No Such Thing as Too Much

test_data = '''20
15
10
5
5'''.split('\n')


def solve(data: List[str], total_amount):
    all_containers = [(i, int(x)) for (i, x) in enumerate(data)]
    # print('all:', all_containers)
    solutions = []

    def dfs(chosen: List, unused: List):
        cont_sum = sum(c[1] for c in chosen)
        if cont_sum == total_amount:
            solutions.append(chosen)
        elif cont_sum < total_amount:
            for pick in unused:
                # Only pick elements later in the list
                dfs([*chosen, pick], [c for c in unused if c[0] > pick[0]])

    dfs([], all_containers)
    # print('solutions:', solutions)
    return solutions


def part1(data: List[str], total_amount):
    return len(solve(data, total_amount))


def part2(data: List[str], total_amount):
    solutions = solve(data, total_amount)
    min_len = min(len(s) for s in solutions)
    return len([s for s in solutions if len(s) == min_len])


def main():
    with open('inputs/day17.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 25)
    assert part1_test_result == 4, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data, 150)
    assert part1_result == 654, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data, 25)
    assert part2_test_result == 3, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data, 150)
    assert part2_result == 57, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
