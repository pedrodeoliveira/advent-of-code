

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


def convert_round_end(response):
    if response == 'X':
        return -1
    elif response == 'Y':
        return 0
    else:
        return 1


def determine_move(p1, round_end):
    if round_end == 0:
        return p1
    if round_end == -1:
        if p1 == 'r':
            return 's'
        elif p1 == 'p':
            return 'r'
        else:
            return 'p'
    else:
        if p1 == 'r':
            return 'p'
        elif p1 == 'p':
            return 's'
        else:
            return 'r'


if __name__ == "__main__":

    with open('input.txt', 'r') as f:

        total_points = 0
        round_nr = 0

        while True:
            line = f.readline()
            line_stripped = line.rstrip()
            if line_stripped == '':
                break

            round_nr += 1

            player1 = line_stripped[0]
            player1 = convert(player1)
            round_end = line_stripped[2]
            round_end = convert_round_end(round_end)
            player2 = determine_move(player1, round_end)

            result = round_result(player1, player2)
            print(f'{round_nr:4d} player1: {player1}, round_end: {round_end:3d}, '
                  f'player2: {player2}, '
                  f'result: {result}')
            total_points += result

        print(f'total_points: {total_points}')
