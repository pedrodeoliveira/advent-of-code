
if __name__ == "__main__":

    elf_max_calories = -1
    max_calories = -1

    calories_dict = {}

    with open('../../days_inputs/day-01.txt', 'r') as f:

        elf = 1
        calories = 0

        while True:
            line = f.readline()

            # remove \n
            line_stripped = line.rstrip()
            if line_stripped == '':

                if calories == 0:
                    break

                # print(f'finished inventory for elf {elf} with total calories: '
                #       f'{calories}')

                # updated dict
                calories_dict[elf] = calories

                elf += 1
                calories = 0
            else:
                # increment the elf calories
                calories += int(line_stripped)

    ordered = {k: v for k, v in sorted(calories_dict.items(), reverse=True, key=lambda item: item[
        1])}

    top_3_elves = list(ordered.keys())[:3]
    print(f'top 3 elves with more calories: {top_3_elves}')
    top_3_total_calories = sum(list(ordered.values())[:3])
    print(f'total calories (top 3 elves): {top_3_total_calories}')

