def part1(puzzle_input: str) -> None:
    result = 0
    ranges: list[tuple[int, int]] = []
    for line in puzzle_input.splitlines():
        if not line:
            ranges = sorted(ranges)
            continue
        if "-" in line:
            start, stop = line.split("-")
            ranges.append((int(start), int(stop)))
            continue

        food_id = int(line)
        for start, stop in ranges:
            if start <= food_id <= stop:
                result += 1
                break
    print(result)


def part2(puzzle_input: str) -> None:
    ranges: list[tuple[int, int]] = []
    for line in puzzle_input.splitlines():
        if not line:
            break
        if "-" in line:
            start, stop = line.split("-")
            ranges.append((int(start), int(stop)))

    attempt = 0
    while True:
        attempt += 1
        changed = False
        new_ranges: set[tuple[int, int]] = set()
        added_ranges: set[int] = set()
        for i, (start1, stop1) in enumerate(ranges):
            if i in added_ranges:
                continue
            found = False
            for j in range(i + 1, len(ranges)):
                if j in added_ranges:
                    continue
                start2, stop2 = ranges[j]
                if (
                    start2 <= start1 <= stop2
                    or start2 <= stop1 <= stop2
                    or start1 <= start2 <= stop1
                    or start1 <= stop2 <= stop1
                ):
                    changed = True
                    found = True
                    new_ranges.add((min(start1, start2), max(stop1, stop2)))
                    added_ranges.add(j)
                    break
            if not found:
                new_ranges.add((start1, stop1))
        ranges = sorted(new_ranges)
        if not changed:
            break

    result = 0
    for start, stop in ranges:
        result += stop - start + 1
    print(result)
