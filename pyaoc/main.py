import sys
from argparse import ArgumentParser
from importlib import import_module
from time import time


def main():
    parser = ArgumentParser()
    parser.add_argument("year", type=int, choices=range(2015, 2024))
    parser.add_argument("day", type=int, choices=range(1, 26))
    parser.add_argument("-s", "--skip", action="store_true", help="skip executing the first part")
    args = parser.parse_args()
    year = str(args.year)
    day = f"{args.day:02}"

    try:
        solution = import_module(f"year{year}.day{day}")
    except ModuleNotFoundError:
        print(f"Cannot find solutions for {year}-{day}")
        sys.exit(1)

    if not args.skip:
        if not hasattr(solution, "part1"):
            print("No solution found for part 1")
            sys.exit(1)

        print()
        print("Part 1:")
        t = time()
        solution.part1()
        d = time() - t
        print(f"Elapsed time: {d:.3f}s")

    if not hasattr(solution, "part2"):
        print("No solution found for part 2")
        sys.exit(1)

    print()
    print("Part 2:")
    t = time()
    solution.part2()
    d = time() - t
    print(f"Elapsed time: {d:.3f}s")


if __name__ == "__main__":
    main()
