from collections import defaultdict
from functools import reduce
from operator import itemgetter, mul

from utils import Point3D


def part1(puzzle_input: str) -> None:
    points = [Point3D(*map(int, line.split(","))) for line in puzzle_input.splitlines()]
    distances: dict[tuple[int, int], float] = {}
    num_points = len(points)
    for i, p1 in enumerate(points):
        for j in range(i + 1, num_points):
            distances[(i, j)] = p1.distance(points[j])

    shortest_distances = [c[0] for c in sorted(distances.items(), key=itemgetter(1))][:1000]
    next_circuit_id = 0
    box_circuit_ids: dict[int, int] = {}
    for box1, box2 in shortest_distances:
        if box1 not in box_circuit_ids and box2 not in box_circuit_ids:
            box_circuit_ids[box1] = next_circuit_id
            box_circuit_ids[box2] = next_circuit_id
            next_circuit_id += 1
        elif box1 in box_circuit_ids and box2 in box_circuit_ids:
            box1_circuit = box_circuit_ids[box1]
            box2_circuit = box_circuit_ids[box2]
            if box1_circuit == box2_circuit:
                continue
            circuit_boxes = [b for b, c in box_circuit_ids.items() if c == box2_circuit]
            for b in circuit_boxes:
                box_circuit_ids[b] = box1_circuit
        elif box1 in box_circuit_ids:
            box_circuit_ids[box2] = box_circuit_ids[box1]
        else:
            box_circuit_ids[box1] = box_circuit_ids[box2]

    circuit_sizes: dict[int, int] = defaultdict(int)
    for _, circuit_id in box_circuit_ids.items():
        circuit_sizes[circuit_id] += 1

    biggest_circuits = sorted(circuit_sizes.items(), key=itemgetter(1), reverse=True)
    result = reduce(mul, [c[1] for c in biggest_circuits[:3]], 1)
    print(result)


def part2(puzzle_input: str) -> None:
    points = [Point3D(*map(int, line.split(","))) for line in puzzle_input.splitlines()]
    distances: dict[tuple[int, int], float] = {}
    num_points = len(points)
    for i, p1 in enumerate(points):
        for j in range(i + 1, num_points):
            distances[(i, j)] = p1.distance(points[j])

    shortest_distances = [c[0] for c in sorted(distances.items(), key=itemgetter(1))]
    next_circuit_id = 0
    box_circuit_ids: dict[int, int] = {}
    for box1, box2 in shortest_distances:
        if box1 not in box_circuit_ids and box2 not in box_circuit_ids:
            box_circuit_ids[box1] = next_circuit_id
            box_circuit_ids[box2] = next_circuit_id
            next_circuit_id += 1
        elif box1 in box_circuit_ids and box2 in box_circuit_ids:
            box1_circuit = box_circuit_ids[box1]
            box2_circuit = box_circuit_ids[box2]
            if box1_circuit == box2_circuit:
                continue
            circuit_boxes = [b for b, c in box_circuit_ids.items() if c == box2_circuit]
            for b in circuit_boxes:
                box_circuit_ids[b] = box1_circuit
        elif box1 in box_circuit_ids:
            box_circuit_ids[box2] = box_circuit_ids[box1]
        else:
            box_circuit_ids[box1] = box_circuit_ids[box2]
        if len(box_circuit_ids) == num_points and len(set(box_circuit_ids.values())) == 1:
            result = points[box1].x * points[box2].x
            print(result)
            return

    print("No answer found")
