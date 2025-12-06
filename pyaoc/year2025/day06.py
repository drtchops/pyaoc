from functools import reduce
from operator import mul


def part1(puzzle_input: str) -> None:
    operators: list[str] = []
    numbers: list[list[int]] = []
    for i, line in enumerate(puzzle_input.splitlines()):
        parts = line.split()
        if i == 0:
            for _ in range(len(parts)):
                numbers.append([])
        if "+" in line:
            operators = parts
            break
        for j, num in enumerate(parts):
            numbers[j].append(int(num))

    result = 0
    for i, operator in enumerate(operators):
        if operator == "+":
            result += sum(numbers[i])
        else:
            result += reduce(mul, numbers[i], 1)
    print(result)


def part2(puzzle_input: str) -> None:
    operators: list[str] = []
    problems: list[list[str]] = []
    widths: list[int] = []
    lines = puzzle_input.splitlines()
    line_width = max(map(len, lines))
    operator_line = lines.pop()
    operator_line = operator_line.ljust(line_width)  # fuck this problem

    current_width = 0
    for character in operator_line:
        if character == " ":
            current_width += 1
            continue
        if current_width:
            widths.append(current_width)
            current_width = 0
        operators.append(character)
        problems.append([])
    widths.append(current_width + 1)

    for line in lines:
        offset = 0
        number_line = line.ljust(line_width)
        for j, width in enumerate(widths):
            problems[j].append(number_line[offset : offset + width])
            offset += width + 1

    result = 0
    for i, operator in enumerate(operators):
        numbers: list[int] = []
        width = widths[i]
        for j in range(widths[i]):
            numbers.append(int("".join(num[j] for num in problems[i])))
        if operator == "+":
            result += sum(numbers)
        else:
            result += reduce(mul, numbers, 1)
    print(result)
