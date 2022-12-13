import json


class Packet:

    def __init__(self, pck_str: str):
        self.pck_str = pck_str
        self.data = json.loads(self.pck_str)

    def __str__(self):
        return self.pck_str

    def __repr__(self):
        return self.pck_str

    def __lt__(self, other):
        return compare(self.data, other.data) < 0


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

    packets = [Packet(line) for line in lines if line != '']
    packets.sort()
    dp1 = Packet('[[2]]')
    dp2 = Packet('[[6]]')
    dp1_idx, dp2_idx = -1, -1
    for i, p in enumerate(packets):
        print(p)
        if p > dp1 and dp1_idx == -1:
            dp1_idx = i+1
        if p > dp2 and dp2_idx == -1:
            dp2_idx = i+2
    decoder_key = dp1_idx * dp2_idx
    print(f'decoder_key: {decoder_key}')
