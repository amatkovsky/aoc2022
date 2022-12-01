def day1(puzzle_input):
    i = 0
    max_calories = 0

    window_calories = 0
    while i < len(puzzle_input):
        cur = puzzle_input[i]
        if cur == '':
            max_calories = max(max_calories, window_calories)
            window_calories = 0
        else:
            window_calories += int(cur)
        i += 1

    print(max_calories)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_1_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day1(puzzle_input)
