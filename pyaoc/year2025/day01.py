def part1(puzzle_input: str) -> None:
    dial = 50
    zero_count = 0
    for line in puzzle_input.splitlines():
        direction = line[0]
        count = int(line[1:])
        if direction == "L":
            dial -= count
        elif direction == "R":
            dial += count
        dial %= 100
        if dial == 0:
            zero_count += 1
    print(zero_count)


def part2(puzzle_input: str) -> None:
    dial = 50
    zero_count = 0
    for line in puzzle_input.splitlines():
        direction = line[0]
        count = int(line[1:])
        click = -1 if direction == "L" else 1
        for _ in range(count):
            dial += click
            dial %= 100
            if dial == 0:
                zero_count += 1
    print(zero_count)
