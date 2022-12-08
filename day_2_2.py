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

    def pick(self, result):
        if result == Result.WIN:
            value = self.value + 1
            return Shape(1 if value > 3 else value)
        elif result == Result.DRAW:
            return self
        elif result == Result.LOSE:
            value = self.value - 1
            return Shape(3 if value < 1 else value)


class Result(Enum):
    LOSE = 1,
    DRAW = 2,
    WIN = 3,


shapes_mapping = {
    'A': Shape.ROCK,
    'B': Shape.PAPER,
    'C': Shape.SCISSORS,
}

result_mapping = {
    'X': Result.LOSE,
    'Y': Result.DRAW,
    'Z': Result.WIN,
}


def day_2(puzzle_input: List[str]):
    score = 0
    for round in puzzle_input:
        shapes = round.split()
        opponent_shape = shapes_mapping[shapes[0]]
        result = result_mapping[shapes[1]]
        my_shape = opponent_shape.pick(result)
        score += my_shape.compare(opponent_shape) + my_shape.value
    print(score)


if __name__ == '__main__':
    puzzle_input = []
    with open('day_2_2_input.txt') as file:
        for line in file:
            puzzle_input.append(line.rstrip())
    day_2(puzzle_input)
