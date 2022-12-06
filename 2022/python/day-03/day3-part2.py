from string import ascii_lowercase, ascii_uppercase


letters = ascii_lowercase + ascii_uppercase
item_priorities = {c: i+1 for i, c in enumerate(letters)}
print(item_priorities)


if __name__ == "__main__":

    with open('../../days_inputs/day-03.txt', 'r') as f:

        total = 0
        line_nr = 0

        nr_groups = 0
        groups = []

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            groups.append(set(line_stripped))

            if len(groups) == 3:
                items_in_common = set.intersection(*groups)
                if len(items_in_common) != 1:
                    print('More than one item in common!')

                item_in_common = items_in_common.pop()
                priority = item_priorities[item_in_common]
                total += priority
                line_nr += 1
                print(f'[{nr_groups: 3d}] item: {item_in_common}, '
                      f'priority: {priority}, total: {total}')

                groups = []
                nr_groups += 1

        print(f'total: {total}')

