

grids = {}
nr_knots = 10


def mark_visited_tail(tail_idx, row, col):
    grids[tail_idx]['r'] = row
    grids[tail_idx]['c'] = col
    grids[tail_idx]['visited'].add((row, col))


def get_tail_indices(tail_idx):
    return grids[tail_idx]['r'], grids[tail_idx]['c']


def is_adjacent(x0, y0, x1, y1):
    return abs(x0-x1) <= 1 and abs(y0-y1) <= 1


def next_tail(x0, y0, x1, y1):
    if y0 == y1:
        return (x0+1, y0) if x1 > x0 else (x0-1, y0)
    elif x0 == x1:
        return (x0, y0+1) if y1 > y0 else (x0, y0-1)
    elif x1 > x0:
        return (x0+1, y0+1) if y1 > y0 else (x0+1, y0-1)
    else:
        return (x0-1, y0+1) if y1 > y0 else (x0-1, y0-1)


def get_next_indices(i, j, direction):
    if direction == 'R':
        i += 1
    elif direction == 'L':
        i -= 1
    elif direction == 'U':
        j += 1
    else:
        j -= 1
    return i, j


def initialize_grids(n):
    for t in range(1, n):
        grids[t] = {
            'r': 0,
            'c': 0,
            'visited': set()
        }
        mark_visited_tail(t, 0, 0)


with open('../../days_inputs/day-09.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    head_r, head_c = 0, 0

    initialize_grids(nr_knots)

    for move in lines:
        direction, size = tuple(move.split())
        size = int(size)

        while size != 0:
            head_r, head_c = get_next_indices(head_r, head_c, direction)

            for tail in range(1, nr_knots):
                # check if T needs to be moved (is adjacent?)
                tail_r, tail_c = get_tail_indices(tail)

                if tail == 1:
                    tail_head_r, tail_head_c = head_r, head_c
                else:
                    tail_head_r, tail_head_c = get_tail_indices(tail-1)

                if not is_adjacent(tail_r, tail_c, tail_head_r, tail_head_c):
                    tail_r, tail_c = next_tail(tail_r, tail_c, tail_head_r, tail_head_c)
                    mark_visited_tail(tail, tail_r, tail_c)

            size -= 1

    print(f'grid size: {len(grids[9]["visited"])}')
