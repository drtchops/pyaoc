from collections import defaultdict
from dataclasses import dataclass


@dataclass
class Wordsearch:
    rows: int
    cols: int
    letters: dict[tuple[int, int], str]


def parse(puzzle_input: str) -> Wordsearch:
    lines = puzzle_input.splitlines()
    search = Wordsearch(
        rows=len(lines),
        cols=len(lines[0]),
        letters=defaultdict(str),
    )
    for y in range(search.rows):
        for x in range(search.cols):
            search.letters[(x, y)] = lines[y][x]
    return search


def part1(puzzle_input: str) -> None:
    search = parse(puzzle_input)
    matches = 0
    for y in range(search.rows):
        for x in range(search.cols):
            if search.letters[(x, y)] != "X":
                continue
            for dy in [-1, 0, 1]:
                for dx in [-1, 0, 1]:
                    if dy == dx == 0:
                        continue
                    if (
                        search.letters[(x + dx, y + dy)] == "M"
                        and search.letters[(x + (2 * dx), y + (2 * dy))] == "A"
                        and search.letters[(x + (3 * dx), y + (3 * dy))] == "S"
                    ):
                        matches += 1
    print(matches)


def part2(puzzle_input: str) -> None:
    search = parse(puzzle_input)
    matches = 0
    for y in range(search.rows):
        for x in range(search.cols):
            if search.letters[(x, y)] != "A":
                continue
            if (
                (search.letters[(x - 1, y - 1)] == "M" and search.letters[(x + 1, y + 1)] == "S")
                or (search.letters[(x - 1, y - 1)] == "S" and search.letters[(x + 1, y + 1)] == "M")
            ) and (
                (search.letters[(x + 1, y - 1)] == "M" and search.letters[(x - 1, y + 1)] == "S")
                or (search.letters[(x + 1, y - 1)] == "S" and search.letters[(x - 1, y + 1)] == "M")
            ):
                matches += 1
    print(matches)
