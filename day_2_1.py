from enum import Enum
from typing import List


class Shape(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    def compare(self, other) -> int:
        if self.value == other.value:
            return 3  # draw
        elif self.value - other.value == 2:
            return 0  # loss
        elif self.value - other.value == -2:
            return 6  # win
        elif self.value < other.value:
            return 0  # loss
        elif self.value > other.value:
            return 6  # win


mapping = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS,
    'X': Shape.ROCK,
    'Y': Shape.PAPER,
    'Z': Shape.SCISSORS,
}


def day_2(puzzle_input: List[str]):
    score = 0
    for round in puzzle_input:
        shapes = round.split()
        opponent_shape = mapping[shapes[0]]
        my_shape = mapping[shapes[1]]
        score += my_shape.compare(opponent_shape) + my_shape.value
    print(score)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_2_1_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day_2(puzzle_input)
