"""Create a function that takes in two parameters: rows, and columns, both of 
which are integers. The function should then proceed to draw a playing board 
(as in the examples from the lectures) the same number of rows and columns as 
specified. After drawing the board, your function should return True."""

def draw_a_board(rows, cols):
    row_len = 2 * rows - 1
    col_len = 2 * cols - 1
    print_this = ''
    
    for i in range(row_len):
        if i % 2 == 0:
            for el in range(col_len):
                if el % 2 == 0:
                    print_this += ' '
                else:
                    print_this +='|'
            print(print_this)
            print_this = ''
        else:
            print('-' * col_len)
    
    return True
    
draw_a_board(3,3)
draw_a_board(5,5)