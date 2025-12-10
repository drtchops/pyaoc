from utils import Point


def part1(puzzle_input: str) -> None:
    tiles = [Point(*map(int, line.split(","))) for line in puzzle_input.splitlines()]
    num_tiles = len(tiles)
    areas: list[int] = []
    for i, t1 in enumerate(tiles):
        for j in range(i + 1, num_tiles):
            t2 = tiles[j]
            areas.append((abs(t1.x - t2.x) + 1) * (abs(t1.y - t2.y) + 1))
    result = max(areas)
    print(result)


def part2(puzzle_input: str) -> None:
    # we're taking advantage of the fact the loop has no "overhangs"
    # I think this is the worst AoC solution I've ever done
    reds = [Point(*map(int, line.split(","))) for line in puzzle_input.splitlines()]
    num_reds = len(reds)
    last_red = reds[0]
    x_spans: dict[int, tuple[int, int]] = {}
    for tile in [*reds[1:], reds[0]]:
        if tile.y in x_spans:
            min_x_span, max_x_span = x_spans[tile.y]
            x_spans[tile.y] = (min(tile.x, min_x_span), max(tile.x, max_x_span))
        else:
            x_spans[tile.y] = (tile.x, tile.x)
        if tile.x == last_red.x:
            top_y = max(tile.y, last_red.y)
            bot_y = min(tile.y, last_red.y)
            for i in range(1, top_y - bot_y):
                green_y = bot_y + i
                if green_y in x_spans:
                    min_x_span, max_x_span = x_spans[green_y]
                    x_spans[green_y] = (min(tile.x, min_x_span), max(tile.x, max_x_span))
                else:
                    x_spans[green_y] = (tile.x, tile.x)
        last_red = tile

    valid_areas: list[int] = []
    for i, t1 in enumerate(reds):
        for j in range(i + 1, num_reds):
            t2 = reds[j]
            min_dx = min(t1.x, t2.x)
            max_dx = max(t1.x, t2.x)
            valid = True
            for dy in range(min(t1.y, t2.y), max(t1.y, t2.y) + 1):
                min_x_span, max_x_span = x_spans[dy]
                if min_dx < min_x_span or min_dx > max_x_span or max_dx < min_x_span or max_dx > max_x_span:
                    valid = False
                    break
            if valid:
                valid_areas.append((abs(t1.x - t2.x) + 1) * (abs(t1.y - t2.y) + 1))
    result = max(valid_areas)
    print(result)
