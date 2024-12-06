import os
import sys
from argparse import ArgumentParser
from importlib import import_module
from time import time
from types import ModuleType
from typing import Any, Literal


def _get_kwargs(solution: ModuleType, year: str, day: str) -> dict[str, Any]:
    solution.__package__
    if int(year) < 2024:
        return {}

    if not solution.__file__:
        print("Cannot find solution path")
        sys.exit(1)
    module_path = os.path.dirname(solution.__file__)
    input_filename = os.path.join(module_path, "input", f"day{day}.txt")
    if not os.path.exists(input_filename):
        print("Cannot find puzzle input file")
        sys.exit(1)
    with open(input_filename) as f:
        return {"puzzle_input": f.read().strip()}


def _run_part(solution: ModuleType, part: Literal[1] | Literal[2], **kwargs: dict[str, Any]):
    func = getattr(solution, f"part{part}", None)
    if not func:
        print(f"No solution found for part {part}")
        sys.exit(1)

    print()
    print(f"Part {part}:")
    t = time()
    func(**kwargs)
    d = time() - t
    print(f"Elapsed time: {d:.3f}s")


def main():
    parser = ArgumentParser()
    parser.add_argument("year", type=int, choices=range(2015, 2025))
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

    kwargs = _get_kwargs(solution, year, day)

    if not args.skip:
        _run_part(solution, 1, **kwargs)
    _run_part(solution, 2, **kwargs)


if __name__ == "__main__":
    main()
