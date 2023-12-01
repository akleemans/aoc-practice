from typing import List, Tuple, Dict

# Day 13: Knights of the Dinner Table

test_data = '''Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.'''.split('\n')


def build_graph(data: List[str]) -> Tuple[List[str], Dict[Tuple[str, str], int]]:
    people = list(set([line.split(' ')[0] for line in data]))
    both_ratings = {}
    for line in data:
        parts = line.split(' ')
        value = int(parts[3])
        if 'lose' in line:
            value = -value
        both_ratings[(parts[0], parts[-1].replace('.', ''))] = value

    ratings = {}
    for i in range(len(people)):
        for j in range(i + 1, len(people)):
            a, b = people[i], people[j]
            ratings[(a, b)] = both_ratings[(a, b)] + both_ratings[(b, a)]
    return people, ratings


def people_from_pairs(pairs: List[Tuple[str, str]]) -> List[str]:
    """Return a list of (possibly duplicated) people from pairs"""
    return [p[0] for p in pairs] + [p[1] for p in pairs]


def solve(people: List[str], ratings: Dict[Tuple[str, str], int]) -> int:
    solutions: List[List[Tuple[str, str]]] = []

    def _dfs(current_pairs: List[Tuple[str, str]]):
        # Only check for neighbors
        all_people = people_from_pairs(current_pairs)
        no_neighbor = [p for p in all_people if all_people.count(p) == 1]
        next_pairs: List[Tuple[str, str]] = [p for p in ratings if p not in current_pairs and (p[0] in no_neighbor or p[1] in no_neighbor)]
        for p in next_pairs:
            possible_solution: List[Tuple[str, str]] = [*current_pairs, p]
            single_people = people_from_pairs(possible_solution)
            if len(possible_solution) == len(people):
                if all([single_people.count(p) == 2 for p in people]):
                    solutions.append(possible_solution)
            elif len(possible_solution) < len(people) and any([single_people.count(p) == 1 for p in people]):
                _dfs(possible_solution)

    # Start with all pairs for a certain person
    start_pairs = [p for p in ratings if people[0] in p]
    for pair in start_pairs:
        _dfs([pair])

    max_score = 0
    for pairs in solutions:
        score = sum([ratings[p] for p in pairs])
        if score > max_score:
            # print('Found higher score!', score, pairs)
            max_score = score

    return max_score


def part1(data: List[str]) -> int:
    people, ratings = build_graph(data)
    return solve(people, ratings)


def part2(data: List[str]):
    people, ratings = build_graph(data)
    for p in people:
        ratings[('Adi', p)] = 0
    people.append('Adi')
    return solve(people, ratings)


def main():
    with open('inputs/day13.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 330, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 664, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 640, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
