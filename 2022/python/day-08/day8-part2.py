import re


# set with all visible trees
# each element is a tuple with (row_idx, column_idx)
trees = {}


def update_tree(row_idx, col_idx, score):
    key = row_idx, col_idx
    if key in trees:
        trees[key] *= score
    else:
        trees[key] = score


def get_scores(arr):
    scores = [0]*len(arr)
    for i, h in enumerate(arr):
        # determine idx of sub array arr[:i] which has the highest height
        # but of at least h
        argmax_i = 0
        for j, hj in enumerate(arr[:i]):
            if hj >= h:
                argmax_i = j
        # print(f'i: {i}, argmax_i: {argmax_i}')
        scores[i] = i - argmax_i
    return scores


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

            # add scores of trees for left to right
            scores = get_scores(r)
            # print(f'LR scores: {scores}')
            for col_idx, score in enumerate(scores):
                update_tree(row_idx, col_idx, score)

            r_copy = r.copy()
            r_copy.reverse()
            scores = get_scores(r_copy)
            # print(f'RL scores: {scores}')
            for rev_col_idx, score in enumerate(scores):
                col_idx = (len(r) - 1) - rev_col_idx
                update_tree(row_idx, col_idx, score)

            row_idx += 1

        for col_idx, col in enumerate(columns):
            scores = get_scores(col)
            for row_idx, score in enumerate(scores):
                update_tree(row_idx, col_idx, score)

            # count visible trees right to left
            c_copy = col.copy()
            c_copy.reverse()
            scores = get_scores(c_copy)
            for rev_row_idx, score in enumerate(scores):
                row_idx = (len(col) - 1) - rev_row_idx
                update_tree(row_idx, col_idx, score)

        # print(trees[(3, 2)])
        # part 2 solution: 230112
        print(max(list(trees.values())))
