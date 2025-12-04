def part1(puzzle_input: str) -> None:
    result = 0
    banks = [list(map(int, line)) for line in puzzle_input.splitlines()]
    for bank in banks:
        max_tens = max(bank[:-1])
        tens_idx = bank.index(max_tens)
        max_ones = max(bank[tens_idx + 1 :])
        result += (max_tens * 10) + max_ones
    print(result)


def part2(puzzle_input: str) -> None:
    result = 0
    banks = [list(map(int, line)) for line in puzzle_input.splitlines()]
    for bank in banks:
        offset = 0
        length = len(bank)
        for i in range(12):
            scope = bank[offset : length - 11 + i]
            digit = max(scope)
            offset += scope.index(digit) + 1
            result += digit * pow(10, 11 - i)
    print(result)
