def parse(puzzle_input: str) -> list[tuple[int, int]]:
    ranges: list[tuple[int, int]] = []
    for entry in puzzle_input.split(","):
        parts = entry.split("-")
        ranges.append((int(parts[0]), int(parts[1])))
    return ranges


def part1(puzzle_input: str) -> None:
    ranges = parse(puzzle_input)
    result = 0
    for min_id, max_id in ranges:
        for current_id in range(min_id, max_id + 1):
            str_id = str(current_id)
            if len(str_id) % 2 == 1:
                continue
            mid = len(str_id) // 2
            if str_id[:mid] == str_id[mid:]:
                result += current_id
    print(result)


def part2(puzzle_input: str) -> None:
    ranges = parse(puzzle_input)
    result = 0
    for min_id, max_id in ranges:
        for current_id in range(min_id, max_id + 1):
            str_id = str(current_id)
            mid = len(str_id) // 2
            for i in range(1, mid + 1):
                if len(str_id) % i != 0:
                    continue
                parts = [str_id[j : j + i] for j in range(0, len(str_id), i)]
                if all(p == parts[0] for p in parts):
                    result += current_id
                    break
    print(result)
