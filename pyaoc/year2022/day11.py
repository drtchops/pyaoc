from dataclasses import dataclass

from pyaoc.utils import lcm


@dataclass
class Monkey:
    idx: int
    items: list[int]
    operator: str = ""
    operationLeft: str = ""
    operationRight: str = ""
    divisor: int = 0
    targetTrue: int = 0
    targetFalse: int = 0
    inspections: int = 0

    def inspect(self, worry: int, relief: bool, multiple: int = 0):
        self.inspections += 1
        left = worry if self.operationLeft == "old" else int(self.operationLeft)
        right = worry if self.operationRight == "old" else int(self.operationRight)
        new_worry = worry
        match self.operator:
            case "+":
                new_worry = left + right
            case "*":
                new_worry = left * right
        if relief:
            new_worry = int(new_worry / 3)
        if multiple:
            new_worry = new_worry % multiple
        target = self.targetTrue if new_worry % self.divisor == 0 else self.targetFalse
        return new_worry, target


def parse():
    monkies: list[Monkey] = []
    monkey: Monkey | None = None
    for line in INPUT.splitlines():
        if line.startswith("Monkey"):
            if monkey:
                monkies.append(monkey)
            monkey = Monkey(idx=len(monkies), items=[])
        if monkey and line.strip().startswith("Starting items: "):
            _, items = line.split(": ")
            monkey.items = list(map(int, items.split(", ")))
        if monkey and line.strip().startswith("Operation: "):
            _, operation = line.split(" = ")
            left, operator, right = operation.split()
            monkey.operationLeft = left
            monkey.operator = operator
            monkey.operationRight = right
        if monkey and line.strip().startswith("Test: "):
            parts = line.split()
            monkey.divisor = int(parts[-1])
        if monkey and line.strip().startswith("If true: "):
            parts = line.split()
            monkey.targetTrue = int(parts[-1])
        if monkey and line.strip().startswith("If false: "):
            parts = line.split()
            monkey.targetFalse = int(parts[-1])

    if monkey:
        monkies.append(monkey)

    return monkies


def process(monkies: list[Monkey], steps: int, relief: bool, multiple: int = 0):
    for i in range(steps):
        for monkey in monkies:
            for _ in range(len(monkey.items)):
                item = monkey.items.pop(0)
                worry, target = monkey.inspect(item, relief, multiple=multiple)
                monkies[target].items.append(worry)


def part1():
    monkies = parse()
    process(monkies, 20, True)
    inspections = sorted([m.inspections for m in monkies], reverse=True)
    print(inspections[0] * inspections[1])


def part2():
    monkies = parse()
    multiple = lcm(
        monkies[0].divisor,
        monkies[1].divisor,
        *[m.divisor for m in monkies[2:]],
    )
    process(monkies, 10000, False, multiple=multiple)
    inspections = sorted([m.inspections for m in monkies], reverse=True)
    print(inspections[0] * inspections[1])


INPUT = """
Monkey 0:
  Starting items: 50, 70, 54, 83, 52, 78
  Operation: new = old * 3
  Test: divisible by 11
    If true: throw to monkey 2
    If false: throw to monkey 7

Monkey 1:
  Starting items: 71, 52, 58, 60, 71
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 0
    If false: throw to monkey 2

Monkey 2:
  Starting items: 66, 56, 56, 94, 60, 86, 73
  Operation: new = old + 1
  Test: divisible by 3
    If true: throw to monkey 7
    If false: throw to monkey 5

Monkey 3:
  Starting items: 83, 99
  Operation: new = old + 8
  Test: divisible by 5
    If true: throw to monkey 6
    If false: throw to monkey 4

Monkey 4:
  Starting items: 98, 98, 79
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 1
    If false: throw to monkey 0

Monkey 5:
  Starting items: 76
  Operation: new = old + 4
  Test: divisible by 13
    If true: throw to monkey 6
    If false: throw to monkey 3

Monkey 6:
  Starting items: 52, 51, 84, 54
  Operation: new = old * 17
  Test: divisible by 19
    If true: throw to monkey 4
    If false: throw to monkey 1

Monkey 7:
  Starting items: 82, 86, 91, 79, 94, 92, 59, 94
  Operation: new = old + 7
  Test: divisible by 2
    If true: throw to monkey 5
    If false: throw to monkey 3
""".strip()
