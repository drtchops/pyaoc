from pyaoc.utils import Point


def part1():
    start: Point
    end: Point
    map: list[list[int]] = []
    for y, line in enumerate(INPUT.splitlines()):
        row = []
        for x, square in enumerate(line):
            if square == "S":
                row.append(1)
                start = Point(x, y)
            elif square == "E":
                row.append(26)
                end = Point(x, y)
            else:
                row.append(ord(square) - 96)
        map.append(row)

    print(map)


def part2():
    pass


INPUT = """
Sabqponm
abcryxxl
accszExk
acctuvwj
abdefghi
""".strip()
