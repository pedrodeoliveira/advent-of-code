

if __name__ == "__main__":

    with open('../../days_inputs/day-01.txt', 'r') as f:

        calibration_value = 0

        while True:
            line = f.readline()

            # remove \n
            line_stripped = line.rstrip()

            if line_stripped == '':
                break

            digits = [d for d in line_stripped if d.isdigit()]
            line_cv = int(f'{digits[0]}{digits[-1]}')
            print(f'line values: {line_cv}')
            calibration_value += line_cv

        print(f'calibration_value: {calibration_value}')
