""" This is Carl Eranio's implimentation of a Hearts Game. 
1.0 Completed: 03AUG2021
Intended changes:
	Create Card and Deck Classes
	Create Computer AI
	Create a GUI Version
	Impliment a internet multiplayer option
 """

from random import shuffle
def cls(): print ("\n" * 42)

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.win_pile = []
        self.hand_score = 0
        self.game_score = 0

    def __str__(self):
        self.Print_Cards(self.hand)
        return (f"{self.name} has 'won' {self.win_pile} sets, a hand score of: {self.hand_score}, \n"
                f"and a game score of {self.game_score}.")

    def Get_Win_Cards(self, cards):
        self.win_pile.append(cards)
        self.Set_Hand_Score(cards)

    def Play_New_Hand(self, cards):
        for card in cards:
            self.hand.append(card)
        self.Organize_Hand()
        self.hand_score = 0

    def I_Have_The_2_of_Clubs(self):
        i_have_2_of_clubs = False
        for card in self.hand:
            if card == ['Club', '2', self.name]:
                    i_have_2_of_clubs = True
        return i_have_2_of_clubs

    def Finish_Old_Hand(self):
        self.game_score += self.hand_score

    def Start_New_Game(self):
        self.game_score = 0
        self.Play_New_Hand()

    def Finish_Set(self, win_pile):
        self.Set_Hand_Score(win_pile)

    def Set_Hand_Score(self, set):
        for card in set:
            if card[0][0] == 'H':
                self.hand_score += 1
            elif card[0][0] == 'S' and card[1][0] == 'Q':
                self.hand_score += 13

    def Print_Cards(self, hand):
        current_hand = []
        for card in hand:
            current_hand.append(self.Ascii_Card_List(card))
        for i in range(5):
            if i != 4:
                for n in range(len(current_hand)):
                    print(current_hand[n][i], end=' ')
            else:
                for n in range(len(current_hand)):
                    if n < 9:
                        print_this = f'  {n + 1}  '
                        print(print_this, end=' ')
                        current_hand[n].append(print_this)
                    else:
                        print_this = f'  {n + 1} '
                        print(print_this, end=' ')
                        current_hand[n].append(print_this)
            print('')
        return current_hand

    def Ascii_Card_List(self, card):
        if card[1] == '10':
            return ['-----',f'|{card[1]} |',f'| {card[0][0]} |', '-----']
        else:
            return ['-----', f'| {card[1][0]} |', f'| {card[0][0]} |', '-----']

    def Organize_Hand(self):
        sorted_hand = []
        card_valu = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        suits = ['Heart', 'Spade', 'Club', 'Diamond']

        while len(sorted_hand) < 13:
            suited_list = []
            for suit in suits:
                lowest_card = 0
                lowest_key = 0
                for card in self.hand:
                    if card[0] == suit:
                        suited_list.append(card)
                for el in card_valu:
                    for suited_card in suited_list:
                        if el == suited_card[1]:
                            sorted_hand.append([suit, el, self.name])
                suited_list = []
        self.hand = sorted_hand



def create_deck(shuffle=True):
    deck = []
    card_valu = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    card_suit = ['Heart', 'Spade', 'Club', 'Diamond']

    for suit in card_suit:
        for valu in card_valu:
            deck.append([suit, valu])

    if shuffle == True:
        try:
            shuffle(deck)
        except:
            try:
                random.shuffle(deck)
            except:
                from random import shuffle
                shuffle(deck)

    return deck


def who_won_this_set(cards):
    winner = 0
    base_suit = cards[0][0]
    highest_card = 0
    for card in cards:
        if card[0] == base_suit:
            try:
                if int(card[1]) > highest_card:
                    highest_card = int(card[1])
                    winner = card[2]
            except:
                ranker = ['Jack', 'Queen', 'King', 'Ace']
                for n in range(len(ranker)):
                    if card[1] == ranker[n]:
                        if 11 + n > highest_card:
                            highest_card = 11 + n
                            winner = card[2]
    for i in range(len(players)):
        if players[i].name == winner:
            return i, players[i].name


def give_cards_to_winner(player_name, cards):
    if player_name == player1.name:
        players[0].Get_Win_Cards(cards)
        return 0
    elif player_name == player2.name:
        players[1].Get_Win_Cards(cards)
        return 1
    elif player_name == player3.name:
        players[2].Get_Win_Cards(cards)
        return 2
    else:
        players[3].Get_Win_Cards(cards)
        return 3


def start_game():
    global players
    game_deck = create_deck()
    msg = "What is your name? "
    player1 = Player(get_players_input(request_for_input=msg))
    player2 = Player(get_players_input(request_for_input=msg))
    player3 = Player(get_players_input(request_for_input=msg))
    player4 = Player(get_players_input(request_for_input=msg))
    players = [player1, player2, player3, player4]
    deal_cards(game_deck)
    pass_cards(0)
    for i in range(len(players)):
        if players[i].I_Have_The_2_of_Clubs():
            return i


def print_cards(hand):
    current_hand = []
    for card in hand:
        current_hand.append(ascii_card_list(card))
    for i in range(5):
        if i != 4:
            for n in range(len(current_hand)):
                print(current_hand[n][i], end=' ')
        else:
            for n in range(len(current_hand)):
                if n < 9:
                    print_this = f'  {n + 1}  '
                    print(print_this, end=' ')
                    current_hand[n].append(print_this)
                else:
                    print_this = f'  {n + 1} '
                    print(print_this, end=' ')
                    current_hand[n].append(print_this)
        print('')


def ascii_card_list(card):
    if card[1] == '10':
        return ['-----',f'|{card[1]} |',f'| {card[0][0]} |', '-----']
    else:
        return ['-----', f'| {card[1][0]} |', f'| {card[0][0]} |', '-----']


def deal_cards(deck):
    hands = [[],[],[],[]]
    for i in range(4):
        for n in range(13):
            hands[i].append(deck.pop())

    players[0].Play_New_Hand(hands[0])
    players[1].Play_New_Hand(hands[1])
    players[2].Play_New_Hand(hands[2])
    players[3].Play_New_Hand(hands[3])


def pass_cards(turn):
    cards_to_pass = [[],[],[],[]]
    pass_direction = ''
    who_has_first = -1
    if turn % 4 == 0:
        pass_direction = -1
    elif turn % 4 == 1:
        pass_direction = 1
    elif turn % 4 == 2:
        pass_direction = 2
    if pass_direction != '':
        for i in range(4):
            input(f"{players[i].name} can only you see the screen? Hit Enter(return) if so. ")
            players[i].Print_Cards(players[i].hand)
            print(f'{players[i].name} which cards do you want to pass to {players[(i + pass_direction) % 4].name}?\n'
                  f'(Indicate by number, 1-13, from left to right, one at a time.) ')
            for n in range(3):
                while True:
                    try:
                        answer = int(input(f'\n{n + 1}: '))
                        break
                    except:
                        print("That wasn't a integer. Please try whole number from 1 to 13: ")

                while answer < 1 or answer > 13:
                    answer = int(input(f'\nNo card {n + 1} was not correct. Please try whole number from 1 to 13: '))

                cards_to_pass[i].append(answer - 1)
            cls()
    for pass_ans in cards_to_pass:
        pass_ans.sort()
        pass_ans.reverse()
    for i in range(4):
        for n in range(3):
            player_from = (i + pass_direction) % 4
            pass_this = cards_to_pass[i][n]
            card_to_xfer = players[player_from].hand.pop(pass_this)
            players[i].hand.append(card_to_xfer)
    for player in players:
        player.Organize_Hand()


def help():
    rules = '''Object of the Game
To be the player with the lowest score at the end of the game. When one
player hits the agreed-upon score or higher, the game ends; and the player
with the lowest score wins.

 
Card Values/Scoring
At the end of each hand, players count the number of hearts they have taken
as well as the queen of spades, if applicable. Hearts count as one point
each and the queen counts 13 points.
Each heart - 1 point
The Queen - 13 points
The aggregate total of all scores for each hand must be a multiple of 26.
The game is usually played to 100 points (some play to 50).
When a player takes all 13 hearts and the queen of spades in one hand,
instead of losing 26 points, that player scores zero and each of his opponents
score an additional 26 points.

 
The Deal
Deal the cards one at a time, face down, clockwise. In a four-player game,
each is dealt 13 cards; in a three-player game, the 2 of diamonds should be
removed, and each player gets 17 cards; in a five-player game, the 2 of
diamonds and 2 of clubs should be removed so that each player will get 10 cards.

 
The Play
The player holding the 2 of clubs after the pass makes the opening lead. If the 
2 has been removed for the three handed game, then the 3 of clubs is led.
 

Each player must follow suit if possible. If a player is void of the suit led, a 
card of any other suit may be discarded. However, if a player has no clubs when the 
first trick is led, a heart or the queen of spades cannot be discarded. The highest 
card of the suit led wins a trick and the winner of that trick leads next. There is 
no trump suit.
The winner of the trick collects it and places it face down. Hearts may not be led 
until a heart or the queen of spades has been discarded. The queen does not have to 
be discarded at the first opportunity.

The queen can be led at any time, except the first round.'''
    print(rules)


def order_players(whos_first):
    player_next = whos_first
    player_order = [[],[],[],[]]
    for i in range(4):
        player_order[i] = player_next
        player_next += 1
        player_next %= 4
    return player_order


def get_players_card_choice(hand_size, print_played_cards,
                            print_hand,extra_msg=None):
    play_this = -1
    while play_this == -1: # user input
        msg = "What card did you want to play?\n"
        if extra_msg != None:
            msg += extra_msg
        try:
            play_this = int(get_players_input(print_played_cards=print_played_cards, players_hand=print_hand,
                                              request_for_input=msg)) - 1

        except:
            print(f"That wasn't a integer. Please try whole number from 1 to {hand_size}: ")
            play_this = -1

        if (play_this < 0) or (play_this > hand_size):
            print(f'\nNo card {play_this + 1} was not correct. Please try whole number from 1 to {hand_size}: ')
            play_this = -1
    return play_this


def get_players_input(print_played_cards=None, players_hand=None, request_for_input='', ):
    player_input = input(request_for_input)
    if player_input == '--help':
        help()
        resume_it = ''
        while resume_it != '--resume':
            resume_it = input("Type --resume to continue ")
        if print_played_cards != None:
            print_hand(print_played_cards)
        if players_hand != None:
            print_hand(players_hand)
        player_input = input(request_for_input)
    return  player_input


def player_has_a_suit(hand, needed_suit):
    for card in hand:
        card_suit = card[0]
        if needed_suit == card_suit:
            return True
    return False


turn = 0
first_to_act = -1
do_what = 'new'
while do_what.lower() != 'quit':
    if do_what.lower() == 'new':
        game_over = False
        turn = 0
        first_to_act = start_game()
        player_order = order_players(first_to_act)
        first_card_played = False
        do_what = 'play hand'
        hearts_broken = False


    if do_what.lower() == 'next': # next game
        turn += 1
        game_deck = create_deck()
        deal_cards(game_deck)
        pass_cards(turn)
        player_order = order_players(first_to_act)
        first_card_played = False
        hearts_broken = False

        do_what = 'play hand'

    if do_what.lower() == 'play hand':
        played_cards = []
        for set in range(13):
            for who_plays in player_order:
                player = players[who_plays]
                first_of_hand = player.name
                cls()
                msg = f"{player.name} can only you see the screen? Hit Enter(return) if so. "
                get_players_input(request_for_input=msg)
                print_cards(played_cards)
                hand = player.Print_Cards(player.hand)
                if first_card_played == True:
                    if len(played_cards) != 0:
                        played_suit = ''
                        correct_suit = played_cards[0][0]
                        play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                        print_hand=hand)
                        played_suit = player.hand[play_this][0]
                        they_are_different = (correct_suit != played_suit)
                        is_in_hand = player_has_a_suit(player.hand, correct_suit)
                        while they_are_different and is_in_hand:
                            msg = f"{player.hand[play_this][1]} of {player.hand[play_this][0]}s is not a " \
                                  f"{correct_suit}. Chose a card of the {correct_suit} suit."
                            play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                        print_hand=hand, extra_msg=msg)
                            played_suit = player.hand[play_this][0]
                            they_are_different = (correct_suit != played_suit)
                    else:

                        play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                    print_hand=hand)
                        if hearts_broken == False:
                            if first_of_hand == player.name:
                                this_cards_suit = player.hand[play_this][0]
                                has_only_hearts = True
                                for card in player.hand:
                                    if card[0] != "Heart":
                                        has_only_hearts = False
                                while (this_cards_suit == 'Heart') and (has_only_hearts == False):
                                    msg = "No hearts have been played, so you can't lead with hearts."
                                    play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                    print_hand=hand, extra_msg=msg)
                                    this_cards_suit = player.hand[play_this][0]
                        elif set == 0:
                            card_suit = player.hand[play_this][0]
                            card_rank = player.hand[play_this][1]
                            while card_suit == 'Spade' and card_rank == "Queen":
                                msg = "You can't play the Queen of Spades in the first set."
                                play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                print_hand=hand, extra_msg=msg)



                else:
                    while (not first_card_played):
                        print()
                        play_this = get_players_card_choice(len(player.hand), print_played_cards=played_cards,
                                                        print_hand=hand)
                        this_cards_suit = player.hand[play_this][0]
                        this_cards_rank = player.hand[play_this][1] == '2'
                        if this_cards_suit == 'Club' and this_cards_rank:
                            first_card_played = True
                        else:
                            print(f"{player.name} that wasn't the 2 of clubs, which must be played first. Please play it.")
                card_to_play = player.hand.pop(play_this)

                played_cards.append(card_to_play)
            first_to_act, hand_winners_name = who_won_this_set(played_cards)
            print(f"{hand_winners_name} won this set.\n")
            players[first_to_act].Finish_Set(played_cards)
            player_order = order_players(first_to_act)
            for player in players:
                print(f"{player.name} has {player.hand_score} points so far, this hand.")
            get_players_input(request_for_input="Press Enter when Ready for Next Set")
            played_cards = []
        do_what = "how hand results"

    if do_what.lower() == "how hand results":
        low_score_player = ''
        low_score_is = 127
        for player in players:
            player.Finish_Old_Hand()
            if player.game_score <= low_score_is:
                if player.game_score == low_score_is:
                    low_score_player = low_score_player + ' and ' + player.name
                else:
                    low_score_player = player.name
                low_score_is = player.game_score
            print(f"{player.name} has {player.game_score} points so far, this game.")
            if player.game_score > 99:
                game_over = True
        if game_over == True:
            print(f"{low_score_player} has won with, {low_score_is}.\n")
            do_what = "game over"
        else:
            do_what = "play hand"
        get_players_input(request_for_input="Press Enter when Ready for Next Set or Hand")

    if do_what.lower() == "game over":
        do_what = get_players_input(request_for_input="""What do you want to do? ('quit', 'new', '--help') """)

