

# Rock: A, X
# Paper: B, Y
# Scissors: C, Z

points = {
    'r': 1,
    'p': 2,
    's': 3
}


def round_result(p1, p2):
    round_points = points[p2]
    if (p2 == 'r' and p1 == 's') or (p2 == 'p' and p1 == 'r') or (p2 == 's' and p1 == 'p'):
        round_points += 6
    if p1 == p2:
        round_points += 3
    return round_points


def convert(response):
    if response == 'A' or response == 'X':
        return 'r'
    elif response == 'B' or response == 'Y':
        return 'p'
    else:
        return 's'


if __name__ == "__main__":

    with open('../../days_inputs/day-02.txt', 'r') as f:

        total_points = 0
        round_nr = 0

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            round_nr += 1

            player1 = line_stripped[0]
            player2 = line_stripped[2]
            player1 = convert(player1)
            player2 = convert(player2)

            result = round_result(player1, player2)
            print(f'{round_nr:4d} player1: {player1}, player2: {player2}, '
                  f'result: {result}')
            total_points += result

        print(f'total_points: {total_points}')
