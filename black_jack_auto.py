from random import shuffle
def cls(): print ("\n" * 100)

BLACK_JACK_PAYS = 2.0

class Player:
    def __init__(self, name, hand=[], money=100):
        self.name = name
        self.hand = hand
        self.score = 0
        self.money = money
        self.bet = 0

    def __str__(self):
        print(f'{self.name} has: ')
        #self.Print_hand(self.hand)
        return ("and a score of: " + str(self.score))


    def Set_Score(self):
        self.score = 0                      # recaculate score from zero
        unbroken_ace = 0                    # to be used to count Aces worth 11 points
        for card in self.hand:
            try:
                self.score += int(card[1])  # if card is numbered no problem
            except:
                if card[1][0] == "A":       # if card is Ace
                    self.score += 11        # add 11
                    unbroken_ace += 1       # increment number of unbroken Aces by 1
                else:
                    self.score += 10        # else, is J - K, and add 10
            if self.score > 21:             # if score greater than 21, and there are aces worth 11,
                if unbroken_ace > 0:        # if there are unbroken aces
                    self.score -= 10        # decrement score by 10
                    unbroken_ace -= 1       # decrement unbroken_ace count by 1
                else:                       # if no aces to decrement
                    return True             # hand is busted
        return False                        # else, hand is not busted

    def Hit(self, card):        # this will recieve a card,
        self.hand.append(card)  # append it to hand,
        self.Set_Score()         # and set the score again

    def Print_hand(self, hand):
        current_hand = []
        for card in hand:
            current_hand.append(self.Ascii_Card_List(card))
        for i in range(4):
            for n in range(len(current_hand)):
                print(current_hand[n][i], end=' ')
            print('')

    def Ascii_Card_List(self, card):
        if card[1] == '10':
            return ['-----',f'|{card[1]} |',f'| {card[0][0]} |', '-----']
        else:
            return ['-----', f'| {card[1][0]} |', f'| {card[0][0]} |', '-----']

    def Play(self, new_hand):
        self.hand = new_hand
        self.Set_Score()

    def Bet_Money(self, amount):
        self.money -= amount
        self.bet += amount

    def Win(self, dealer_score, dealer_hand):
        lost = False
        if self.score > 21:
            lost = True
        elif dealer_score > self.score and not dealer_score > 21:
            lost = True
        elif dealer_score == self.score: # both scores are equal
            if dealer_hand == 2 and len(self.hand) == 2: # and in case both hit black jack
                self.money = self.bet   # push
            elif self.score == 21 and len(self.hand) == 2: # or if both didn't hit black jack but the player did
                self.money = self.bet * BLACK_JACK_PAYS # pay extra
            elif dealer_hand == 2: # or if deal hit black jack, but player didn't
                lost = True
            else: # they both have the same score, and neither have black jack
                self.money = self.bet
            self.bet = 0 # reset bet in all cases.
        else: # all other cases, player won
            self.money += self.bet * 2
        self.bet = 0

        return lost

    def Print_Dealer(self, card):
        current_hand = []
        current_hand.append(self.Ascii_Card_List(card))
        for i in range(4):
            for n in range(len(current_hand)):
                print(current_hand[n][i], end=' ')
            print('')

        dealer_score = 0
        try:
            dealer_score += int(card)  # if card is numbered no problem
        except:
            if card[1][0] == "A":       # if card is Ace
                dealer_score += 11        # add 11      # increment number of unbroken Aces by 1
            else:
                dealer_score+= 10        # else, is J - K, and add 10
        print(f'Dealer show\'s a score of: {dealer_score}')



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




game_deck = create_deck()
carl = Player('Carl', [game_deck.pop(0), game_deck.pop(0)], 0)
dealer = Player('Dealer', [game_deck.pop(), game_deck.pop()])
for i in range(100000000):
    carl.Set_Score()
    #dealer.Print_Dealer(dealer.hand[0])
    carl.Bet_Money(1)
    #print(carl)
    while carl.score < 21:
        hit_it = 'y' if carl.score < 17 else 'n'
        if hit_it.lower() == 'y':
            carl.Hit(game_deck.pop())
        else:
            break

        #dealer.Print_Dealer(dealer.hand[0])
        carl.Set_Score()
        #print(carl)

    dealer.Set_Score()
    while dealer.score < 17:
        dealer.Hit(game_deck.pop())
        dealer.Set_Score()

    # if not (carl.Win(dealer.score, dealer.hand)):
    #     print(f'You win! Your score was {carl.score}, and the dealers score was {dealer.score}!')
    #     print(f'You have ${carl.money}')
    # else:
    #     print(f'You lost! Your score was {carl.score}, and the dealers score was {dealer.score}.')
    #     print(f'You have ${carl.money}')



    game_deck = create_deck()
    carl.Play([game_deck.pop(), game_deck.pop()])
    dealer.Play([game_deck.pop(),game_deck.pop()])


print(carl)
