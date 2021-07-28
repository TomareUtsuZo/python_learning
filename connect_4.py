"""This is to create a Connect 4 game."""

def draw_a_board(rows, cols, played_positions):
    row_len = 2 * rows
    col_len = 2 * cols - 1
    print_this = ''

    for row in range(row_len):
        if row % 2 == 0:
            print_this = str(int(row/2)) + '->'
            for col in range(col_len):
                if col % 2 == 0:
                    print_this += played_positions[int(row/2)][int(col/2)]
                else:
                    print_this +='|'
            print(print_this)
            print_this = ''
        else:
            if row == row_len - 1:
                bottom_map = ''
                for i in range(col_len):
                    if i % 2 == 0:
                        bottom_map = bottom_map + str(int(i/2)) +' '
                print('   ' + bottom_map)
            else:
                print('   ' + '-' * col_len)


def get_player_input(player=1):
    done = False
    while done is not True:
        drop_where = int(input(f'What column do you want to drop your peice into, player {player}? '))
        if drop_where > 4:
            draw_a_board(5, 5, game_space)
            print(f"Yeah, there are no column {drop_where}'s, dumbass.")
        elif game_space[0][drop_where] == ' ':
            done = True
            for i in range(-1,-6, -1):
                if game_space[i][drop_where] == ' ':
                    game_space[i][drop_where] =  "X" if player == 1 else "O"
                    break
        else:
            draw_a_board(5, 5, game_space)
            print("Yeah, that space is already filled. Could you go back and chose a new column?")


def check_for_win():
    # horizontal check
    for i in game_space:
        test = ''.join(i)
        if 'XXXX' in test:
            return True
        if 'OOOO' in test:
            return True
    # vertical check
    for col in range(5):
        test = ''
        for row in range(5):
            test += game_space[row][col]
        if 'XXXX' in test:
            return True
        if 'OOOO' in test:
            return True
    # diagonal
    diag_right = [[],[],[],[],[]]
    diag_left = [[],[],[],[],[]]
    for i in range(5):
        for n in range(4 - i):
            diag_right[i].append(' ')
        for el in game_space[i]:
            diag_right[i].append(el)
    for i in range(5):
        for n in range(i):
            diag_left[i].append(' ')
        for el in game_space[i]:
            diag_left[i].append(el)
    test1 = ''
    test2 = ''
    for col in range(2,5):
        for row in range(5):
            test1 += diag_right[row][col]
            test2 += diag_left[row][col]
        if 'XXXX' in test1:
            return True
        if 'OOOO' in test1:
            return True
        if 'XXXX' in test2:
            return True
        if 'OOOO' in test2:
            return True

game_running = True
player_is = 2
game_turn = 1
game_space = [[' ',' ',' ', ' ', ' '],[' ',' ',' ', ' ', ' '],
                  [' ',' ',' ', ' ', ' '], [' ',' ',' ', ' ', ' '], [' ',' ',' ', ' ', ' ']]

while(game_running is True):
    player_is = 1 if player_is == 2 else 2
    draw_a_board(5, 5, game_space)
    get_player_input(player_is)
    game_turn += 1
    if game_turn > 7:
        if check_for_win():
            game_running = False
            print(f"Player {player_is} won!")

