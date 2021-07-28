

gallows0 = """
                        -----
                        |    |
                        |
                        |
                        |
                        |
                        |
                    -----------"""
gallows1 = """
                        -----
                        |    |
                        |   |-|
                        |   
                        |    
                        |
                        |
                    -----------"""
gallows2 = """
                        -----
                        |    |
                        |   {-}
                        | >_| |_<
                        |   | |
                        |
                        |
                    -----------"""
gallows3 = """
                        -----
                        |    |
                        |   {-}
                        | >_| |_<
                        |   | |
                        |   /
                        |  <
                    -----------"""
gallows4 = """
                        -----
                        |    |
                        |   {-}
                        | >_| |_<
                        |   | |
                        |   / \
                        |  <   >
                    -----------"""

gallows_list = [gallows0, gallows1, gallows2, gallows3, gallows4]

def draw_game_board(display_word, misses):
    print(chr(27) + "[2J")
    print(gallows_list[misses] + ' \n \n')
    print()
    print(display_word)


def mask_word(word_to_mask):
    display_word = ''
    for el in word_to_mask:
        if el.isalpha():
            display_word += '*'
        else:
            display_word += ' '
    return display_word


def test_word(letter_to_test, word_under_test, display_word):
    is_in = True
    if letter_to_test in word_under_test and letter_to_test not in display_word:
        for i in range(len(word_under_test)):
            if word_under_test[i] == letter_to_test:
                display_word = display_word[0:i] + letter_to_test + display_word[i+1: ]
    else:
        is_in = False
    return is_in, display_word


def test_for_end(guessed_right, guesses, word):
    game_on = True
    if guessed_right == False:
        guesses += 1
        if guesses < 4:
            print("oooff, that is not what he wanted to see")
        else:
            print("damn... that poor sod")
            game_on = False
    elif '*' not in word:
        print(f'You\'re right! The word was {word}.')
        print('You saved your buddy!!')
        game_on = False
    return game_on, guesses

guesses_wrong = 0
keep_going = True
player1_word = (input("What do you want the other player to guess at? ")).lower()
display_word = mask_word((player1_word))

while keep_going:
    correct_guess = True
    draw_game_board(display_word, guesses_wrong)
    player2_input = (input('What guess do you want to make? ')).lower()
    correct_guess, display_word = test_word(player2_input, player1_word, display_word)
    keep_going, guesses_wrong = test_for_end(correct_guess, guesses_wrong, display_word)



