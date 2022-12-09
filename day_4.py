from typing import List


def is_subset(set1: List[int], set2: List[int]) -> bool:
    return set1[0] >= set2[0] and set1[1] <= set2[1]


def overlaps(set1: List[int], set2: List[int]) -> bool:
    return set2[0] <= set1[1] <= set2[1]


def day_4_1(puzzle_input):
    inclusive_pairs = 0
    for row in puzzle_input:
        pairs = row.split(',')

        pair1 = pairs[0]
        pair2 = pairs[1]

        bounds1 = list(map(lambda x: int(x), pair1.split('-')))
        bounds2 = list(map(lambda x: int(x), pair2.split('-')))

        if is_subset(bounds1, bounds2) or is_subset(bounds2, bounds1):
            inclusive_pairs += 1
    print(inclusive_pairs)


def day_4_2(puzzle_input):
    overlapping_pairs = 0
    for row in puzzle_input:
        pairs = row.split(',')

        pair1 = pairs[0]
        pair2 = pairs[1]

        bounds1 = list(map(lambda x: int(x), pair1.split('-')))
        bounds2 = list(map(lambda x: int(x), pair2.split('-')))

        if overlaps(bounds1, bounds2) or overlaps(bounds2, bounds1):
            overlapping_pairs += 1
    print(overlapping_pairs)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_4_1_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day_4_2(puzzle_input)
