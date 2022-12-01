def day1(puzzle_input):
    i = 0
    top_3_max_calories = []

    window_calories = 0
    while i < len(puzzle_input):
        cur = puzzle_input[i]
        if cur == '':
            top_3_max_calories.append(window_calories)
            window_calories = 0
        else:
            window_calories += int(cur)
        i += 1
    top_3_max_calories.append(window_calories)

    top_3_max_calories.sort(reverse=True)
    j = 0
    top_3_calories_sum = 0
    while j < min(len(top_3_max_calories), 3):
        top_3_calories_sum += top_3_max_calories[j]
        j += 1
    print(top_3_calories_sum)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_1_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day1(puzzle_input)
