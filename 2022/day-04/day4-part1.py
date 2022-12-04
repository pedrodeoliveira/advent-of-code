

if __name__ == "__main__":

    with open('input.txt', 'r') as f:

        total = 0
        line_nr = 0

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            left, right = tuple(line_stripped.split(','))
            left_min, left_max = tuple(left.split('-'))
            left_min = int(left_min)
            left_max = int(left_max)
            right_min, right_max = tuple(right.split('-'))
            right_min = int(right_min)
            right_max = int(right_max)

            if left_min <= right_min and left_max >= right_max:
                print(f'found pair [{line_nr:3d}] {left} + {right}')
                total += 1
            elif right_min <= left_min and right_max >= left_max:
                print(f'found pair [{line_nr:3d}] {left} + {right}')
                total += 1
            else:
                print(f'[{line_nr:3d}] {left} + {right}')

            line_nr += 1

        print(f'total: {total}')

