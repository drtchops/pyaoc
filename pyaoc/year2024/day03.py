import re


def part1(puzzle_input: str) -> None:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)", puzzle_input.strip())
    total = 0
    for m in matches:
        parts = m[4:-1].split(",")
        total += int(parts[0]) * int(parts[1])
    print(total)


def part2(puzzle_input: str) -> None:
    matches = re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", puzzle_input.strip())
    total = 0
    enabled = True
    for m in matches:
        if m == "do()":
            enabled = True
        elif m == "don't()":
            enabled = False
        elif enabled:
            parts = m[4:-1].split(",")
            total += int(parts[0]) * int(parts[1])
    print(total)
