from collections import Counter


def part1(puzzle_input: str) -> None:
    beams: set[int] = set()
    beam_count = 0
    for line in puzzle_input.splitlines():
        for i, character in enumerate(line):
            if character == "S":
                beams.add(i)
            elif character == "^" and i in beams:
                beam_count += 1
                beams.remove(i)
                for dx in (-1, 1):
                    if i + dx not in beams:
                        beams.add(i + dx)
    print(beam_count)


def part2(puzzle_input: str) -> None:
    beams: Counter[int] = Counter()
    beam_count = 1
    for line in puzzle_input.splitlines():
        new_beams: Counter[int] = Counter()
        for i, character in enumerate(line):
            if character == "S":
                beams[i] += 1
            elif character == "^":
                beam_count += beams[i]
                for dx in (-1, 1):
                    new_beams[i + dx] += beams[i]
                beams[i] = 0
        beams += new_beams
    print(beam_count)
