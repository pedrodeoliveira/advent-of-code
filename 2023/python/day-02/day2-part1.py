import re


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
            game_is_valid = True
            for s in sets:
                # Use a regular expression to find pairs of (number, color)
                matches = re.findall(r'(\d+)\s+(\w+)', s)
                # Create a dictionary from the matches
                result_dict = {color: int(number) for number, color in matches}
                if not is_set_valid(result_dict):
                    game_is_valid = False
                    break

            if game_is_valid:
                total += game_idx

        print(f'total: {total}')
