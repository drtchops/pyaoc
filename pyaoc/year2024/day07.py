from itertools import product


def parse(puzzle_input: str) -> list[tuple[int, list[int]]]:
    equations: list[tuple[int, list[int]]] = []
    for line in puzzle_input.splitlines():
        result, rest = line.split(": ")
        values = [int(i) for i in rest.split()]
        equations.append((int(result), values))
    return equations


def test_operators(result: int, values: list[int], all_operators: list[str]) -> bool:
    for operators in product(all_operators, repeat=len(values) - 1):
        val = values[0]
        for i, op in enumerate(operators):
            if op == "+":
                val += values[i + 1]
            elif op == "*":
                val *= values[i + 1]
            elif op == "|":
                val = int(str(val) + str(values[i + 1]))
        if val == result:
            return True
    return False


def part1(puzzle_input: str) -> None:
    total = 0
    for result, values in parse(puzzle_input):
        if test_operators(result, values, ["+", "*"]):
            total += result
    print(total)


def part2(puzzle_input: str) -> None:
    total = 0
    for result, values in parse(puzzle_input):
        if test_operators(result, values, ["+", "*", "|"]):
            total += result
    print(total)
