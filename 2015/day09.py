from typing import List

# Day 9: All in a Single Night

test_data = '''London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141'''.split('\n')


class Node:
    def __init__(self, name):
        self.neighbors = {}
        self.name = name

    def __str__(self):
        return self.name + '(' + str([k.name + ':' + str(v) for k, v in self.neighbors.items()]) + ')'

    def __repr__(self):
        return self.__str__()


def build_nodes(data) -> List[Node]:
    nodes = []
    nodes_dict = {}
    # First, create all nodes
    for line in data:
        parts = line.split(' ')
        for name in [parts[0], parts[2]]:
            if name not in nodes_dict:
                n = Node(name)
                nodes_dict[name] = n
                nodes.append(n)
    # Then, link them
    for line in data:
        parts = line.split(' ')
        n0 = nodes_dict[parts[0]]
        n1 = nodes_dict[parts[2]]
        dist = int(parts[4])
        n0.neighbors[n1] = dist
        n1.neighbors[n0] = dist
    return nodes


def solve(data: List[str], f):
    nodes = build_nodes(data)
    # List of possible paths with distances
    queue = [([n], 0) for n in nodes]
    best_dist = 0 if f.__name__ == 'max' else 10 ** 6
    while len(queue) > 0:
        current_path, current_dist = queue.pop()
        if len(current_path) == len(nodes):
            best_dist = f(best_dist, current_dist)
            continue
        # Add paths
        current_node = current_path[-1]
        for neighbor in current_node.neighbors.keys():
            if neighbor not in current_path:
                new_dist = current_dist + current_node.neighbors[neighbor]
                queue.append((current_path + [neighbor], new_dist))
    return best_dist


def part1(data: List[str]):
    return solve(data, min)


def part2(data: List[str]):
    return solve(data, max)


def main():
    with open('inputs/day09.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 605, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 117, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data)
    assert part2_test_result == 982, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 909, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
