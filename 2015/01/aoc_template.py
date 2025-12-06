# aoc_template.py

import pathlib
import sys

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input

def part1(data):
    """Solve part 1."""

    return len(data) - 2 * data.count(")")

def part2(data):
    """Solve part 2."""
    floor = 0

    for i, char in enumerate(data):
        if char == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            return i + 1

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