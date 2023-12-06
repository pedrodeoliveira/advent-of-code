import re
from functools import reduce


def is_set_valid(d):
    if d.get('red', 0) > 12 or d.get('green', 0) > 13 or d.get('blue', 0) > 14:
        return False
    return True


if __name__ == "__main__":

    with open('../../days_inputs/day-02.txt', 'r') as f:

        total = 0

        while True:
            line = f.readline()

            # remove \n
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            game_str, sets_str = tuple(line_stripped.split(':'))
            game_idx = int(re.findall(r'\d+', game_str)[0])
            sets = sets_str.split(';')

            game_minimum = {"red": 0, "green": 0, "blue": 0}
            for s in sets:
                # Use a regular expression to find pairs of (number, color)
                matches = re.findall(r'(\d+)\s+(\w+)', s)
                # Create a dictionary from the matches
                result_dict = {color: int(number) for number, color in matches}
                for color, count in result_dict.items():
                    if game_minimum[color] < count:
                        game_minimum[color] = count
            game_power = reduce(lambda x, y: x * y, game_minimum.values())
            total += game_power

        print(f'total: {total}')
