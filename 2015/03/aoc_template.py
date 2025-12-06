# aoc_template.py

import pathlib
import sys

sys.setrecursionlimit(10000)

DIRECTIONS = {"^": (-1, 0), ">": (0, 1), "v": (1, 0), "<": (0, -1)}
MAP_SIZE = 150

def move(x, y, map, movements):
    if len(movements) == 0:
        return
    
    dx, dy = DIRECTIONS[movements[0]]
    nx, ny = x + dx, y + dy
    
    map[nx][ny] = 1

    return move(nx, ny, map, movements[1:])

def parse(puzzle_input):
    """Parse input."""

    return puzzle_input

def part1(data):
    """Solve part 1."""
    map = [([0] * (2 * MAP_SIZE + 1)) for _ in range(2 * MAP_SIZE + 1)]
    map[MAP_SIZE][MAP_SIZE] = 1
    move(MAP_SIZE, MAP_SIZE, map, data)

    return sum([sum(row) for row in map])

def part2(data):
    """Solve part 2."""
    map = [([0] * (2 * MAP_SIZE + 1)) for _ in range(2 * MAP_SIZE + 1)]
    map[MAP_SIZE][MAP_SIZE] = 1
    move(MAP_SIZE, MAP_SIZE, map, data[0::2])
    move(MAP_SIZE, MAP_SIZE, map, data[1::2])

    return sum([sum(row) for row in map])

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