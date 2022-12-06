from string import ascii_lowercase, ascii_uppercase


letters = ascii_lowercase + ascii_uppercase
item_priorities = {c: i+1 for i, c in enumerate(letters)}
print(item_priorities)


if __name__ == "__main__":

    with open('../../days_inputs/day-03.txt', 'r') as f:

        total = 0
        line_nr = 0

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            n = int(len(line_stripped)/2)
            left = set(line_stripped[:n])
            right = set(line_stripped[n:])
            items_in_common = left.intersection(right)
            if len(items_in_common) != 1:
                print('More than one item in common!')

            item_in_common = items_in_common.pop()
            priority = item_priorities[item_in_common]
            total += priority
            line_nr += 1
            print(f'[{line_nr:3d}] {left} + {right}, item: {item_in_common}, '
                  f'priority: {priority}, total: {total}')

        print(f'total: {total}')

