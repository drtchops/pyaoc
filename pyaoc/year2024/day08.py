from dataclasses import dataclass
from itertools import combinations

from utils import Point


@dataclass
class Grid:
    width: int
    height: int
    nodes: dict[str, list[Point]]


def parse(puzzle_input: str) -> Grid:
    lines = puzzle_input.splitlines()
    height = len(lines)
    width = len(lines[0])
    nodes: dict[str, list[Point]] = {}
    for y, line in enumerate(lines):
        for x, label in enumerate(line):
            if label != ".":
                nodes.setdefault(label, []).append(Point(x, y))
    return Grid(
        width=width,
        height=height,
        nodes=nodes,
    )


def part1(puzzle_input: str) -> None:
    grid = parse(puzzle_input)
    antinodes: set[Point] = set()
    for nodes in grid.nodes.values():
        if len(nodes) < 2:
            continue
        for first, second in combinations(nodes, 2):
            delta = second - first
            first_anti = first - delta
            second_anti = second + delta
            if first_anti.x >= 0 and first_anti.x < grid.width and first_anti.y >= 0 and first_anti.y < grid.height:
                antinodes.add(first_anti)
            if second_anti.x >= 0 and second_anti.x < grid.width and second_anti.y >= 0 and second_anti.y < grid.height:
                antinodes.add(second_anti)
    print(len(antinodes))


def part2(puzzle_input: str) -> None:
    grid = parse(puzzle_input)
    antinodes: set[Point] = set()
    for nodes in grid.nodes.values():
        if len(nodes) < 2:
            continue
        for first, second in combinations(nodes, 2):
            antinodes.add(first)
            antinodes.add(second)
            delta = second - first
            anti = first - delta
            while anti.x >= 0 and anti.x < grid.width and anti.y >= 0 and anti.y < grid.height:
                antinodes.add(anti)
                anti -= delta
            anti = second + delta
            while anti.x >= 0 and anti.x < grid.width and anti.y >= 0 and anti.y < grid.height:
                antinodes.add(anti)
                anti += delta
    print(len(antinodes))
