from dataclasses import dataclass
from enum import Enum, auto

from utils import Point


class Direction(Enum):
    UP = auto()
    RIGHT = auto()
    DOWN = auto()
    LEFT = auto()


@dataclass
class Map:
    width: int
    height: int
    start_pos: Point
    start_dir: Direction
    walls: set[Point]


deltas = {
    Direction.UP: Point(0, -1),
    Direction.RIGHT: Point(1, 0),
    Direction.DOWN: Point(0, 1),
    Direction.LEFT: Point(-1, 0),
}
next_dirs = {
    Direction.UP: Direction.RIGHT,
    Direction.RIGHT: Direction.DOWN,
    Direction.DOWN: Direction.LEFT,
    Direction.LEFT: Direction.UP,
}


def parse(puzzle_input: str) -> Map:
    lines = puzzle_input.splitlines()
    width = len(lines[0])
    height = len(lines)
    start_pos = Point(0, 0)
    start_dir = Direction.UP
    walls: set[Point] = set()

    for y, line in enumerate(lines):
        for x, mark in enumerate(line):
            if mark == "#":
                walls.add(Point(x, y))
            elif mark == "^":
                start_dir = Direction.UP
                start_pos = Point(x, y)
            elif mark == ">":
                start_dir = Direction.RIGHT
                start_pos = Point(x, y)
            elif mark == "v":
                start_dir = Direction.DOWN
                start_pos = Point(x, y)
            elif mark == "<":
                start_dir = Direction.LEFT
                start_pos = Point(x, y)

    return Map(width=width, height=height, start_pos=start_pos, start_dir=start_dir, walls=walls)


def part1(puzzle_input: str) -> None:
    guard_map = parse(puzzle_input)
    visited: set[Point] = set()
    pos = guard_map.start_pos
    direction = guard_map.start_dir
    while True:
        if pos.x < 0 or pos.x >= guard_map.width or pos.y < 0 or pos.y >= guard_map.height:
            break
        visited.add(pos)
        next_pos = pos + deltas[direction]
        if next_pos in guard_map.walls:
            direction = next_dirs[direction]
        else:
            pos = next_pos

    print(len(visited))


def navigate(guard_map: Map) -> bool:
    visited: set[tuple[Point, Direction]] = set()
    pos = guard_map.start_pos
    direction = guard_map.start_dir
    while True:
        if pos.x < 0 or pos.x >= guard_map.width or pos.y < 0 or pos.y >= guard_map.height:
            return False
        if (pos, direction) in visited:
            return True
        visited.add((pos, direction))
        next_pos = pos + deltas[direction]
        if next_pos in guard_map.walls:
            direction = next_dirs[direction]
        else:
            pos = next_pos


def part2(puzzle_input: str) -> None:
    guard_map = parse(puzzle_input)
    count = 0
    for y in range(guard_map.height):
        for x in range(guard_map.width):
            p = Point(x, y)
            if p != guard_map.start_pos and p not in guard_map.walls:
                guard_map.walls.add(p)
                if navigate(guard_map):
                    count += 1
                guard_map.walls.remove(p)

    print(count)
