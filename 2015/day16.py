from typing import List


# Day 16: Aunt Sue

class Sue:
    def __init__(self, idx, properties):
        self.idx = idx
        self.properties = properties


def parse_input(data):
    sues = []
    for line in data:
        idx = int(line.split(':')[0].split(' ')[1])
        properties = {'children': -1, 'cats': -1, 'samoyeds': -1, 'pomeranians': -1, 'akitas': -1, 'vizslas': -1,
                      'goldfish': -1, 'trees': -1, 'cars': -1, 'perfumes': -1}
        for prop in line.split(','):
            prop = prop.strip().split(' ')
            amount = int(prop[-1])
            name = prop[-2].replace(':', '')
            properties[name] = amount
        sues.append(Sue(idx, properties))
    return sues


requirements = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5,
                'trees': 3, 'cars': 2, 'perfumes': 1}


def part1(data: List[str]):
    sues = parse_input(data)
    for sue in sues:
        correct_sue = True
        for req in requirements:
            if sue.properties[req] not in (-1, requirements[req]):
                correct_sue = False
                break
        if correct_sue:
            return sue.idx


def part2(data: List[str]):
    sues = parse_input(data)
    for sue in sues:
        correct_sue = True
        for req in requirements:
            if sue.properties[req] == -1:
                continue
            if req in ['cats', 'trees']:
                if sue.properties[req] <= requirements[req]:
                    correct_sue = False
            elif req in ['pomeranians', 'goldfish']:
                if sue.properties[req] >= requirements[req]:
                    correct_sue = False
            elif sue.properties[req] != requirements[req]:
                correct_sue = False
            if not correct_sue:
                break

        if correct_sue:
            return sue.idx


def main():
    with open('inputs/day16.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_result = part1(data)
    assert part1_result == 103, f'Part 1 returned {part1_result}'

    part2_result = part2(data)
    assert part2_result == 405, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
