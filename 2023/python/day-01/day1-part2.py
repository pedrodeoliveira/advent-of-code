import re


def digit_to_number(digit):
    if len(digit) == 1:
        return int(digit)
    word_to_num_mapping = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
    }
    return word_to_num_mapping.get(digit.lower(), None)


string_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
string_digits += [str(i) for i in range(1, 10)]

if __name__ == "__main__":

    with open('../../days_inputs/day-01.txt', 'r') as f:

        calibration_value = 0

        while True:
            line = f.readline()

            # remove \n
            line_stripped = line.rstrip()

            if line_stripped == '':
                break

            pattern = r"(?=("+'|'.join(string_digits)+r"))"
            digits_found = re.findall(pattern, line_stripped)
            line_cv = int(f'{digit_to_number(digits_found[0])}{digit_to_number(digits_found[-1])}')
            print(f'line values: {line_cv}')
            calibration_value += line_cv

        print(f'calibration_value: {calibration_value}')
