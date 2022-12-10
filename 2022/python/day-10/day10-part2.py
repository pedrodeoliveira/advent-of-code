

with open('../../days_inputs/day-10.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    nr_cycles = 0
    x = 1

    cycles_of_interest = [c for c in range(40, 280, 40)]

    total = 0
    crt_row = ''

    for instruction in lines:
        # print(f'>>>[{instruction}]')

        if instruction == 'noop':
            # print(f'[cycle={nr_cycles:3d}] x: {x}')
            nr_cycles += 1

            # draw pixel at position nr_cycle - 1
            position = (nr_cycles - 1) % 40
            pixel = '#' if abs(x-position) <= 1 else '.'
            # print(f'position: {position}, sprite: {[x-1, x, x+1]}, pixel: {pixel}')
            crt_row = f'{crt_row}{pixel}'
            # print(f'crt_row: {crt_row}')

            if nr_cycles in cycles_of_interest:
                print(f'{crt_row}')
                # print(position % 40)
                crt_row = ''
        else:
            op, op_cycles = tuple(instruction.split())
            op_cycles = int(op_cycles)
            for _ in range(2):
                # print(f'[cycle={nr_cycles:3d}] x: {x}')
                nr_cycles += 1

                # draw pixel at position nr_cycle - 1
                position = (nr_cycles - 1) % 40
                pixel = '#' if abs(x - position) <= 1 else '.'
                # print(f'position: {position}, sprite: {[x - 1, x, x + 1]}, pixel: {pixel}')
                crt_row = f'{crt_row}{pixel}'
                # print(f'crt_row: {crt_row}')

                if nr_cycles in cycles_of_interest:
                    print(f'{crt_row}')
                    # print(position % 40)
                    crt_row = ''

            x += op_cycles
    # print(f'total: {total}')
