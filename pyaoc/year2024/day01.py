from collections import Counter


def parse(puzzle_input: str) -> tuple[list[int], list[int]]:
    left_ids: list[int] = []
    right_ids: list[int] = []
    for line in puzzle_input.splitlines():
        if not line:
            continue
        left_num, right_num = line.split()
        left_ids.append(int(left_num))
        right_ids.append(int(right_num))

    return left_ids, right_ids


def part1(puzzle_input: str) -> None:
    left_ids, right_ids = parse(puzzle_input)
    left_ids = sorted(left_ids)
    right_ids = sorted(right_ids)
    distance = sum(abs(left_id - right_id) for left_id, right_id in zip(left_ids, right_ids, strict=True))
    print(distance)


def part2(puzzle_input: str) -> None:
    left_ids, right_ids = parse(puzzle_input)
    right_counts = Counter(right_ids)
    similarity = sum(left_id * right_counts[left_id] for left_id in left_ids)
    print(similarity)
