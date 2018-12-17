#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

from random import shuffle

# Two useful variables for creating Cards.
SUITE = 'Hearts Diamonds Spades Clubs'.split()
RANKS = 'Ace 2 3 4 5 6 7 8 9 10 Jack Queen King'.split()

class Deck():

    card_list = []
    """
    This is the Deck Class. This object will create a deck of cards to initiate
    play. You can then use this Deck list of cards to split in half and give to
    the players. It will use SUITE and RANKS to create the deck. It should also
    have a method for splitting/cutting the deck in half and Shuffling the deck.
    """
    def __init__(self):
        for face in SUITE:
            for num in RANKS:
                Deck.card_list.append(num + " of " + face)

        print("Deck of Cards have been created.")

    def __str__(self):
        return str(Deck.card_list)
    
    def distribute_cards(self):
        card_len = len(Deck.card_list)
        return [Deck.card_list[:card_len//2],Deck.card_list[card_len//2:]]

    def shuffle_deck(self):
        return shuffle(Deck.card_list)

    def cut_deck(self,rot):
        new_array, l = [], len(Deck.card_list)
        mov_index = rot
        for i in Deck.card_list:
            new_array.append(Deck.card_list[mov_index % l])
            mov_index += 1
            i = i
        return new_array
        

class Hand(Deck):
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    def __init__(self):
        self.cards_in_hand = []

    def __str__(self):
        return str(self.cards_in_hand)

    def add_to_hand(self):
        self.cards_in_hand.append()

    #def remove_from_hand():

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """
    def __init__(self, pname,player_hand):
        self.player_name = pname
        self.player_hand = player_hand
        print(self.player_name + " has joined the game")
        for i in range(len(Deck.card_list)//2):
            self.player_hand.cards_in_hand.append(Deck.card_list[i])
        print(self.player_name + " has taken his cards")


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
deck = Deck()
deck.shuffle_deck()

phand1 = Hand()
p1 = Player("Dhaval", phand1)




# Use the 3 classes along with some logic to play a game of war!
