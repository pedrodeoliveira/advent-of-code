import re


# set with all visible trees
# each element is a tuple with (row_idx, column_idx)
trees = set()


def get_visible_indices(arr):
    n = len(arr)
    max_h = arr[0]
    visible = [0]
    for i in range(1, n-1):
        h = arr[i]
        if h > max_h:
            visible.append(i)
        max_h = max(h, max_h)
    return visible


if __name__ == "__main__":

    with open('../../days_inputs/day-08.txt', 'r') as f:

        rows = []
        columns = []

        row_idx = 0

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            r = [int(i) for i in re.findall(r'\d', line_stripped)]
            rows.append(r)
            if len(columns) == 0:
                columns = [[] for _ in range(len(r))]

            for i, h in enumerate(r):
                columns[i].append(h)

            # count visible trees left to right
            for col_idx in get_visible_indices(r):
                tree = (row_idx, col_idx)
                # print(f'LR: {tree}')
                trees.add(tree)

            # print(f'LR: {trees}')

            # count visible trees right to left
            r_copy = r.copy()
            r_copy.reverse()
            for rev_col_idx in get_visible_indices(r_copy):
                col_idx = (len(r) - 1) - rev_col_idx
                tree = (row_idx, col_idx)
                # print(f'RL: {tree}')
                trees.add(tree)

            # increment column index
            row_idx += 1

        # print(rows)
        # print(columns)

        for col_idx, col in enumerate(columns):
            for row_idx in get_visible_indices(col):
                trees.add((row_idx, col_idx))

            # count visible trees right to left
            c_copy = col.copy()
            c_copy.reverse()
            for rev_row_idx in get_visible_indices(c_copy):
                row_idx = (len(col) - 1) - rev_row_idx
                trees.add((row_idx, col_idx))

        # print(trees)
        # part 1 solution: 1845
        print(f'nr_visible: {len(trees)}')


