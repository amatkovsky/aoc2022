def get_priority(char):
    if char.islower():
        return 1 + (ord(char) - ord('a'))
    else:
        return 27 + (ord(char) - ord('A'))


def day_3_1(puzzle_input):
    priority_sum = 0
    for rucksack in puzzle_input:
        compartment_1 = set(rucksack[:len(rucksack) // 2])
        compartment_2 = set(rucksack[len(rucksack) // 2:])
        dupes = compartment_1 & compartment_2
        for d in dupes:
            priority_sum += get_priority(d)

    print(priority_sum)


def day_3_2(puzzle_input):
    priority_sum = 0
    i = 0
    while i < len(puzzle_input):
        group1 = puzzle_input[i]
        group2 = puzzle_input[i + 1]
        group3 = puzzle_input[i + 2]

        dupes = set(group1) & set(group2) & set(group3)

        assert len(dupes) == 1

        priority_sum += get_priority(dupes.pop())

        i += 3
    print(priority_sum)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_3_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day_3_2(puzzle_input)
