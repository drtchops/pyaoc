def parse(puzzle_input: str) -> list[int]:
    fs: list[int] = []
    file_id = 0
    is_file = True
    for s in puzzle_input:
        num = int(s)
        to_add = [file_id] if is_file else [-1]
        fs.extend(to_add * num)
        if is_file:
            file_id += 1
        is_file = not is_file
    return fs


def part1(puzzle_input: str) -> None:
    fs = parse(puzzle_input)
    free_idx = 0
    file_idx = len(fs) - 1
    total = 0
    while file_idx >= free_idx:
        while fs[free_idx] != -1:
            total += free_idx * fs[free_idx]
            free_idx += 1
        while fs[file_idx] == -1:
            file_idx -= 1
        fs[free_idx] = fs[file_idx]
        fs[file_idx] = -1
    print(total)


def part2(puzzle_input: str) -> None:
    pass
