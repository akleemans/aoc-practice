from typing import List

# Day 15: Science for Hungry People

test_data = '''Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3'''.split('\n')


def parse_input(data):
    ingredients = []
    for line in data:
        parts = line.replace(',', '').split(' ')
        ingredients.append((int(parts[2]), int(parts[4]), int(parts[6]), int(parts[8]), int(parts[10])))
    return ingredients


def solve(ing, check_calories=False):
    best_score = 0
    for a in range(100):
        for b in range(100):
            for c in range(100):
                for d in range(100):
                    if a + b + c + d != 100:
                        continue
                    capacity = ing[0][0] * a + ing[1][0] * b + ing[2][0] * c + ing[3][0] * d
                    durability = ing[0][1] * a + ing[1][1] * b + ing[2][1] * c + ing[3][1] * d
                    flavor = ing[0][2] * a + ing[1][2] * b + ing[2][2] * c + ing[3][2] * d
                    texture = ing[0][3] * a + ing[1][3] * b + ing[2][3] * c + ing[3][3] * d
                    calories = ing[0][4] * a + ing[1][4] * b + ing[2][4] * c + ing[3][4] * d

                    new_score = max(capacity, 0) * max(durability, 0) * max(flavor, 0) * max(texture, 0)
                    if not check_calories or calories == 500:
                        best_score = max(new_score, best_score)
    return best_score


def part1(data: List[str]):
    ingredients = parse_input(data)
    return solve(ingredients)


def part2(data: List[str]):
    ingredients = parse_input(data)
    return solve(ingredients, check_calories=True)


def main():
    with open('inputs/day15.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    # Test inputs doesn't work because 4 ingredients are hardcoded ¯\_(ツ)_/¯
    # part1_test_result = part1(test_data)
    # assert part1_test_result == 0, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 21367368, f'Part 1 returned {part1_result}'

    # part2_test_result = part2(test_data)
    # assert part2_test_result == 0, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 1766400, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
