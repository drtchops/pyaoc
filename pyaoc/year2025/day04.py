def parse(puzzle_input: str) -> dict[tuple[int, int], bool]:
    return {(x, y): point == "@" for y, row in enumerate(puzzle_input.splitlines()) for x, point in enumerate(row)}


def part1(puzzle_input: str) -> None:
    paper_map = parse(puzzle_input)
    result = 0
    for (x, y), point in paper_map.items():
        if not point:
            continue
        count = 0
        for dx in (-1, 0, 1):
            for dy in (-1, 0, 1):
                if dx == 0 and dy == 0:
                    continue
                if paper_map.get((x + dx, y + dy)):
                    count += 1
                if count >= 4:
                    break
        if count < 4:
            result += 1

    print(result)


def part2(puzzle_input: str) -> None:
    paper_map = parse(puzzle_input)
    result = 0
    while True:
        iteration_result = 0
        for (x, y), point in paper_map.items():
            if not point:
                continue
            count = 0
            for dx in (-1, 0, 1):
                for dy in (-1, 0, 1):
                    if dx == 0 and dy == 0:
                        continue
                    if paper_map.get((x + dx, y + dy)):
                        count += 1
                    if count >= 4:
                        break
            if count < 4:
                iteration_result += 1
                paper_map[(x, y)] = False
        result += iteration_result
        if iteration_result == 0:
            break
    print(result)
