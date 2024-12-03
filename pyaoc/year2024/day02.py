def parse(puzzle_input: str) -> list[list[int]]:
    reports: list[list[int]] = []
    for line in puzzle_input.splitlines():
        if not line:
            continue
        reports.append([int(i) for i in line.split()])
    return reports


def is_safe(report: list[int]) -> bool:
    increasing = False
    decreasing = False
    for i in range(1, len(report)):
        curr = report[i]
        prev = report[i - 1]
        if curr == prev:
            return False
        if curr > prev:
            increasing = True
            if decreasing:
                return False
        else:
            decreasing = True
            if increasing:
                return False
        if abs(curr - prev) > 3:
            return False
    return True


def part1(puzzle_input: str) -> None:
    reports = parse(puzzle_input)
    safe_count = sum(1 for report in reports if is_safe(report))
    print(safe_count)


def is_safe_with_dampener(report: list[int]) -> bool:
    if is_safe(report):
        return True
    for i in range(len(report)):
        if is_safe(report[0:i] + report[i + 1 :]):
            return True
    return False


def part2(puzzle_input: str) -> None:
    reports = parse(puzzle_input)
    safe_count = sum(1 for report in reports if is_safe_with_dampener(report))
    print(safe_count)
