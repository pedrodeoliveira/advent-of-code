

with open('../../days_inputs/day-10.txt', 'r') as f:
    lines = [s.rstrip() for s in f.readlines()]
    print(f'read {len(lines)} lines')

    nr_cycles = 0
    x = 1

    cycles_of_interest = [c for c in range(20, 260, 40)]

    total = 0

    for instruction in lines:
        # print(f'>>>[{instruction}]')
        if instruction == 'noop':
            # print(f'[cycle={nr_cycles:3d}] x: {x}')
            nr_cycles += 1
            if nr_cycles in cycles_of_interest:
                signal_strength = nr_cycles * x
                total += signal_strength
                print(f'nr_cycles: {nr_cycles:3d}, x: {x:2d}, signal_strength:'
                      f' {signal_strength:5d}, total: {total:5d}')
        else:
            op, op_cycles = tuple(instruction.split())
            op_cycles = int(op_cycles)
            for _ in range(2):
                # print(f'[cycle={nr_cycles:3d}] x: {x}')
                nr_cycles += 1
                if nr_cycles in cycles_of_interest:
                    signal_strength = nr_cycles * x
                    total += signal_strength
                    print(f'nr_cycles: {nr_cycles:3d}, x: {x:2d}, signal_strength:'
                          f' {signal_strength:5d}, total: {total:5d}')

            x += op_cycles

    print(f'total: {total}')
