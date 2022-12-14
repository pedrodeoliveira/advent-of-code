import json


class Packet:

    def __init__(self, pck_str: str):
        self.pck_str = pck_str
        self.data = json.loads(self.pck_str)

    def __str__(self):
        return self.pck_str


def compare(left, right):
    # print(f'Comparing {left} with {right}')
    if type(left) == int and type(right) == int:
        if left == right:
            return 0
        return -1 if left < right else 1
    elif type(left) == list and type(right) == int:
        return compare(left, [right])
    elif type(left) == int and type(right) == list:
        return compare([left], right)
    else:
        N = min(len(left), len(right))
        for i in range(N):
            result = compare(left[i], right[i])
            if result != 0:
                return result

        if len(left) == len(right):
            # print('no more items to process')
            return 0
        elif len(left) < len(right):
            # print('left does not have more items')
            return -1
        else:
            # print('right does not have more items')
            return 1


with open('../../days_inputs/day-13.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    # print(f'read {len(lines)} lines')

    pairs = []
    curr_pair = None
    for line in lines:
        if curr_pair is None:
            curr_pair = Packet(line), None
        elif line != '':
            curr_pair = curr_pair[0], Packet(line)
            pairs.append(curr_pair)
        else:
            curr_pair = None

    total = 0
    for i, pair in enumerate(pairs):
        p1, p2 = pair
        # in_order = is_in_right_order(p1, p2)
        result = compare(p1.data, p2.data)
        print(f'result: {result}')
        in_order = result == -1
        if in_order:
            total += i+1
        print(f'pair: {i+1:2d}, in order: {in_order}')
    print(f'total: {total}')


