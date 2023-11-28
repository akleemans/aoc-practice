from typing import List

# Day 5: Doesn't He Have Intern-Elves For This?

test_data = '''ugknbfddgicrmopn
aaa
jchzalrnumimnmhp
haegwjzuvuyypxyu
dvszwmarrgswjxmb'''.split('\n')

test_data2 = '''qjhvhtzxzqqjkmpb
xxyxx
uurcxstgmygtbstg
ieodomkazucvgmuy'''.split('\n')


def part1(data: List[str]):
    count = 0
    for word in data:
        vowel_count = 0
        double_letter = False
        bad_strings = False
        for i in range(len(word)):
            c = word[i]
            if c in 'aeiou':
                vowel_count += 1
            if i >= 1 and c == word[i - 1]:
                double_letter = True
        if 'ab' in word or 'cd' in word or 'pq' in word or 'xy' in word:
            bad_strings = True
        if vowel_count >= 3 and double_letter and not bad_strings:
            count += 1
    return count


def part2(data: List[str]):
    count = 0
    for word in data:
        letter_between = False
        repeating_pair = False
        for i in range(len(word) - 2):
            if word[i] == word[i + 2]:
                letter_between = True
            pair = word[i] + word[i + 1]
            if len(word.split(pair)) >= 3:
                repeating_pair = True

        if letter_between and repeating_pair:
            count += 1
    return count


def main():
    with open('inputs/day05.txt') as read_file:
        data = [x.rstrip('\n') for x in read_file.readlines()]

    part1_test_result = part1(test_data)
    assert part1_test_result == 2, f'Part 1 test input returned {part1_test_result}'
    part1_result = part1(data)
    assert part1_result == 236, f'Part 1 returned {part1_result}'

    part2_test_result = part2(test_data2)
    assert part2_test_result == 2, f'Part 2 test input returned {part2_test_result}'
    part2_result = part2(data)
    assert part2_result == 51, f'Part 2 returned {part2_result}'


if __name__ == '__main__':
    main()
