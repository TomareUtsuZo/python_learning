import sys

def draw_a_board(rows, cols, played_positions=[]):
    try:
        rows = int(rows)
        row_len = 2 * rows
    except ValueError:
        print(f"Passed non-number values to rows: '{rows}'.")
        new_row = ''
        for el in rows:
            if el.isnumeric():
                new_row += el
        try:
            rows = int(new_row)
            row_len = 2 * int(rows)
        except:
            print('Yeah, you really messed that up.')
            sys.exit(1)
        print("I think I fixed it for you, otherwise, go back and put the right numbers in the rows.")

    try:
        cols = int(cols)
        col_len = 2 * cols - 1
    except:
        print(f"Passed non-number values to cols: '{cols}'")
        new_col = ''
        for el in cols:
            if el.isnumeric():
                new_col += el
        try:
            cols = int(new_col)
            col_len = 2 * int(cols) - 1
        except:
            print('Yeah, you really messed that up.')
            sys.exit(1)
        print("I think I fixed it for you, otherwise, go back and put the right numbers in the cols.")

    print_this = ''

    for row in range(row_len):
        if row % 2 == 0:
            print_this = str(int(row/2)) + '->'
            for col in range(col_len):
                if col % 2 == 0:
                    try:
                        print_this += played_positions[int(row/2)][int(col/2)]
                    except:
                        played_positions = [[' '] * cols for i in range(rows)]
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


draw_a_board(3,3)
draw_a_board(3,'3')
draw_a_board(3,'3x')
draw_a_board('3', 3)
draw_a_board('3x', 3)
draw_a_board(3,'')
