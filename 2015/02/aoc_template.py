# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""

    return [[int(x) for x in row.split("x")] for row in puzzle_input.splitlines()]

def part1(data):
    """Solve part 1."""
    sum = 0

    for l, w, h in data:
        paper = 2 * l * w + 2 * w * h + 2 * h * l
        slack = min(l * w, w * h, h * l)
        sum += paper + slack

    return sum


def part2(data):
    """Solve part 2."""
    sum = 0

    for l, w, h in data:
        ribbon = 2 * min(l + w, w + h, h + l)
        bow = l * w * h
        sum += ribbon + bow

    return sum

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))