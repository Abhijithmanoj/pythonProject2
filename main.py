# War Game
import random
#Global Variables
suits = ('Diamonds','Hearts','Spades', 'Clubs')
ranks=('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values={'Two': 2, 'Three': 3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}
class Cards():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suit

"""k_of_h=Cards('Hearts','King')
print(k_of_h)
j_of_c=Cards("Hearts","Jack")
print(j_of_c)"""
class Deck():
    def __init__(self):
        self.all_cards=[] #all 52 cards will be stored here
        for suit in suits:
            for rank in ranks:
                card=Cards(suit,rank)
                self.all_cards.append(card)
    def shuffle(self):
        random.shuffle(self.all_cards)
    def take_one(self):
        return self.all_cards.pop()
d=Deck()
print(d.all_cards[0])
d.shuffle()
print(d.all_cards[0])
class Player():
    def __init__(self,name):
        self.name=name
        self.cards_in_hand = []
    def add_cards(self,newcards):
        """ Add cards to back.. (end)"""
        if type(newcards) == type([]):
            #if a list of cads are added
            self.cards_in_hand.extend(newcards)
        else:
            #one card only
            self.cards_in_hand.append(newcards)
    def remove_cards(self):
        """ Remove card from front ..(top)"""
        return self.cards_in_hand.pop(0)
    def __str__(self):
        return f'{self.name} has {len(self.cards_in_hand)} cards. '
#setup
player1=Player("One")
player2=Player("Two")
new_deck=Deck()
new_deck.shuffle()
for x in range (26):
    player1.add_cards(new_deck.take_one())
    player2.add_cards(new_deck.take_one())
game_on=True
round_no=0
while game_on:
    round_no += 1
    print(f'Round {round_no}')
    if len(player1.cards_in_hand) == 0:
        print("Player 1,out of cards...Player 2 Wins!!!")
        game_on=False
        break
    if len(player2.cards_in_hand) == 0:
        print("Player 2,out of cards...Player 1 Wins!!!")
        game_on = False
        break
    player1_cards=[]
    player1_cards.append(player1.remove_cards())
    player2_cards=[]
    player2_cards.append(player2.remove_cards())

    war=True
    while war:
        if player1_cards[-1].value > player2_cards[-1].value:
            player1.add_cards(player1_cards)
            player1.add_cards(player2_cards)
            war=False
        elif player1_cards[-1].value < player2_cards[-1].value:
            player2.add_cards(player1_cards)
            player2.add_cards(player2_cards)
            war=False
        else:
            print("WAR")
            if len(player1.cards_in_hand) < 6:
                print("Player 1 doesn't have enough cards")
                print("Player 2 Wins!!!")
                game_on=False
                break
            elif len(player2.cards_in_hand) < 6:
                print("Player 2 doesn't have enough cards")
                print("Player 1 Wins!!!")
                game_on=False
                break
            else:
                for n in range(3):
                    player1_cards.append(player1.remove_cards())
                    player2_cards.append((player2.remove_cards()))
