

if __name__ == "__main__":

    elf_max_calories = -1
    max_calories = -1

    with open('../input.txt', 'r') as f:

        elf = 1
        calories = 0

        while True:
            line = f.readline()

            # remove \n
            line_stripped = line.rstrip()
            if line_stripped == '':

                if calories == 0:
                    break

                print(f'finished inventory for elf {elf} with total calories: '
                      f'{calories}')

                if calories > max_calories:
                    elf_max_calories = elf
                    max_calories = calories
                    print(f'  >> new elf {elf_max_calories} with max calories: {max_calories}')

                elf += 1
                calories = 0
            else:
                # increment the elf calories
                calories += int(line_stripped)

    print(f'elf {elf_max_calories} with max calories: {max_calories}')
