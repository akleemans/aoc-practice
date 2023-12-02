from typing import List, Tuple

# Day 14: Reindeer Olympics

test_data = '''Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.'''.split('\n')


def parse_input(data):
    reindeers = []
    for line in data:
        parts = line.split(' ')
        reindeers.append((int(parts[3]), int(parts[6]), int(parts[13])))
    return reindeers


def get_distances(reindeers: List[Tuple[int, int, int]], seconds):
    distances = []
    for reindeer in reindeers:
        speed, duration, rest = reindeer
        # Modulo time up to before end of time
        cycle = duration + rest
        distance = (seconds // cycle) * speed * duration
        # Add remainder
        m = seconds % cycle
        distance += speed * min(m, duration)
        distances.append(distance)
    return distances


def part1(data: List[str], seconds):
    reindeers = parse_input(data)
    distances = get_distances(reindeers, seconds)
    return max(distances)


class Reindeer:

    def __init__(self, speed, duration, rest):
        self.points = 0
        self.t = 0
        self.distance = 0
        self.speed = speed
        self.duration = duration
        self.rest = rest
        self.cycle = duration + rest

    def tick(self):
        if self.t % self.cycle < self.duration:
            self.distance += self.speed
        self.t += 1

    def award_point(self, lead_distance):
        if self.distance == lead_distance:
            self.points += 1


def simulate_race(reindeers, seconds):
    reindeers = [Reindeer(*r) for r in reindeers]
    for t in range(seconds):
        [r.tick() for r in reindeers]
        max_distance = max([r.distance for r in reindeers])
        [r.award_point(max_distance) for r in reindeers]

    return [r.points for r in reindeers]


def part2(data: List[str], seconds):
    reindeers = parse_input(data)
    points = simulate_race(reindeers, seconds)
    return max(points)


def main():
    with open('inputs/day14.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data, 1000)
    assert part1_test_result == 1120, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data, 2503)
    assert part1_result == 2696, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data, 1000)
    assert part2_test_result == 689, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data, 2503)
    assert part2_result == 1084, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
