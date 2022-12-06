from collections import deque
import re


if __name__ == "__main__":

    with open('input.txt', 'r') as f:

        total = 0
        line_nr = 0

        stack_lines = deque()

        # create initial stacks
        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            print(f'1 - {line_stripped}')
            stack_lines.appendleft(line_stripped)

        stack_indices_line = stack_lines.popleft()
        stack_indices = [i for i, c in enumerate(stack_indices_line) if c.isnumeric()]

        stacks = {}
        for i in range(len(stack_indices)):
            stacks[i+1] = deque()

        for item in stack_lines:
            for i, idx in enumerate(stack_indices):
                crate = item[idx]
                if crate.isalpha():
                    stacks[i+1].append(crate)

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            numbers = [int(s) for s in re.findall(r'\d+', line_stripped)]
            if len(numbers) != 3:
                print(numbers)
            nr_crates, from_stack, to_stack = tuple(numbers)

            temp_stack = deque()
            while nr_crates != 0:
                crate = stacks[from_stack].pop()
                temp_stack.appendleft(crate)
                nr_crates -= 1

            while len(temp_stack) != 0:
                crate = temp_stack.popleft()
                stacks[to_stack].append(crate)

        for i in range(len(stack_indices)):
            crate = stacks[i+1].pop()
            print(crate, end='')
        print()

