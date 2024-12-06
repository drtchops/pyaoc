from collections import defaultdict
from math import floor


def parse(puzzle_input: str) -> tuple[dict[int, set[int]], list[list[int]]]:
    deps: dict[int, set[int]] = defaultdict(set)
    updates: list[list[int]] = []
    deps_done = False
    for line in puzzle_input.splitlines():
        if not line:
            deps_done = True
            continue

        if deps_done:
            updates.append([int(i) for i in line.split(",")])
        else:
            first, second = line.split("|")
            deps[int(second)].add(int(first))

    return deps, updates


def validate(update: list[int], deps: dict[int, set[int]]) -> bool:
    seen: set[int] = set()
    in_update = set(update)
    for n in update:
        if (deps[n] & in_update) - seen:
            return False
        seen.add(n)
    return True


def part1(puzzle_input: str) -> None:
    deps, updates = parse(puzzle_input)
    total = 0
    for update in updates:
        if validate(update, deps):
            total += update[floor(len(update) / 2)]
    print(total)


def fix(update: list[int], deps: dict[int, set[int]]) -> list[int]:
    while not validate(update, deps):
        for i in range(len(update)):
            n = update[i]
            max_index = max([update.index(m) for m in deps[n] if m in update], default=len(update))
            if max_index > i:
                update = update[:i] + update[i + 1 : max_index + 1] + [n] + update[max_index + 1 :]
                break
    return update


def part2(puzzle_input: str) -> None:
    deps, updates = parse(puzzle_input)
    total = 0
    for update in updates:
        if validate(update, deps):
            continue
        total += fix(update, deps)[floor(len(update) / 2)]
    print(total)
