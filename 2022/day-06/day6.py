

def find_marker(datastream, nr_chars):
    for i, c in enumerate(datastream):
        if i < nr_chars:
            continue
        last_sequence = line_stripped[i - nr_chars:i]
        # print(f'[{i:4d}] {last_sequence}')

        if len(set(last_sequence)) == nr_chars:
            print(f'found marker {last_sequence} at char nr {i}')
            return i


if __name__ == "__main__":

    with open('input.txt', 'r') as f:

        # create initial stacks
        line = f.readline()
        line_stripped = line.rstrip()

        # part 1
        find_marker(line_stripped, nr_chars=4)
        # part 2
        find_marker(line_stripped, nr_chars=14)
