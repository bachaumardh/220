"""
Name: Hugo Bachaumard
lab10.py

Problem: Showing ability to practice constructs and built-in lis functions.

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def main():
    pass


def create_board(row, col):
    output = []
    for i in range(row):
        row = []
        for j in range(col):
            row.append(0)
        output.append(row)
    return output


def display(game):
    for i in range(3):
        print("{}|{}|{}".format(game[i][0], game[i][1], game[i][2]))
        if i != 2:
            print("-----")


def check_move(game, value):
    if game[value // 3][value % 3] == 'X' or game[value // 3][value % 3] == 'O':
        return False
    return True


def check_win(game, player):
    for i in range(3):
        game_win = True
        for j in range(3):
            if game[i][j] != player:
                game_win = False
                continue

        if game_win:
            return game_win

    for i in range(3):
        game_win = True
        for j in range(3):
            if game[j][i] != player:
                game_win = False
                continue

        if game_win:
            return game_win

    game_win = True
    for i in range(3):
        if game[i][i] != player:
            game_win = False

    if game_win:
        return game_win

    game_win = True

    if game[0][2] != player or game[1][1] != player or game[2][0] != player:
        game_win = False

    return game_win


def play_game():
    piece = ['X', 'O']
    number = ['1', '2']
    game = create_board(3, 3)
    for i in range(3):
        for j in range(3):
            game[i][j] = i * 3 + j + 1

    player = 0
    display(game)

    for i in range(9):
        print()
        while True:
            value = int(input("Player {}'s move:".format(number[player]))) - 1
            if check_move(game, value):
                game[value // 3][value % 3] = piece[player]
                break
            else:
                print("Not a valid move! Try again.")
        display(game)

        if check_win(game, piece[player]):
            return "Player {} wins!".format(number[player])
        player = 1 - player

    return "Tied Game!"


print(play_game())


main()
