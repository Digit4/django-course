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

from random import shuffle, choice
from time import sleep

# Two useful variables for creating Cards.
SUITE = 'H D S C'.split()
RANKS = 'A 2 3 4 5 6 7 8 9 10 J Q K'.split()

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
        division = card_len // 2
        other = card_len - division
        return [Deck.card_list[:division],Deck.card_list[other:]]

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

    hand_num = 0

    def __init__(self):
        self.cards_in_hand = Deck.distribute_cards(self)[Hand.hand_num]
        Hand.hand_num += 1

    def __str__(self):
        return str(self.cards_in_hand)
    
    def __len__(self):
        return len(self.cards_in_hand)

    def check_hand(self, card):
        for i in self.cards_in_hand:
            if(card == i):
                return True
        return False

    def remove_from_hand(self, card):
        self.cards_in_hand.remove(card)
    
    def add_to_hand(self, card):
        self.cards_in_hand.append(card)

class Player(Hand):
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The Payer can then play cards and check if they still have cards.
    """

    def remove_from_hand(self, card):
        super(Hand, self).remove_from_hand(card)
        
    def add_to_hand(self, card):
        super(Hand, self).add_to_hand(card)

    def __init__(self, pname):
        self.player_name = pname
        self.player_hand = Hand()
        print(self.player_name + " has joined the game")
        print(self.player_name + " has taken his cards")

    def __str__(self):
        return ("Player Name:" + self.player_name + " has " + ",".join(self.player_hand.cards_in_hand) + "\n")


######################
#### GAME PLAY #######
######################
print("Welcome to War, let's begin...")
deck = Deck()
deck.shuffle_deck()

def check_suite(string):
    if (string == "h" or string == "s" or string == "d" or string == "c"):
        return string.upper()
    else:
        return False        

def rank_reversal(val):
    if (type(val) == type("aaa")):
        val = int(val)
    if (val == 11):
        return "J"
    elif (val == 12):
        return "Q"
    elif (val == 13):
        return "K"
    elif (val == 14):
        return "A"
    else:
        return str(val)

def check_rank(string):
    string = string.lower()
    if (string.isnumeric()):
        return int(string)
    else:
        if (string == "qqq"):
            exit(0)
        if (string == "a"):
            return 14
        elif (string == "k"):
            return 13
        elif (string == "q"):
            return 12
        elif (string == "j"):
            return 11
        else:
            return 0

def parser(string):
    hand = list(map(str, string.split()))
    rank = check_rank(hand[0].lower())
    suite = check_suite(hand[-1].lower())
    if (not suite):
        print("Please enter appropriate suite.")
    else:
        if (rank != 0):
            return [rank,suite]
        else:
            print("Please enter valid input")

pname = input("Enter player's name:")
p1 = Player(pname)
p2 = Player("Computer")

cards_on_hold = []

game_over = False

while (not game_over):
    print(p1.player_name + "'s Turn. Please select a card to play.")
    print(p1.player_hand)
    ch = input("Keep values space seperated:")
    r = parser(ch)
    sleep(1)
    
    if (r == None):
        continue
    else:
        player_card = rank_reversal(r[0]) + " of " + r[1]
        if (p1.player_hand.check_hand(player_card)):
            print("%s played %s" % (p1.player_name, player_card))
        else:
            print("you do not have this card.")
            continue
        print("Computer's turn...")
        comp_card = "5 of S"#choice(RANKS) + " of " + choice(SUITE)
        while (not p2.player_hand.check_hand(comp_card)):
            comp_card = choice(RANKS) + " of " + choice(SUITE)
        print("%s played %s" % (p2.player_name, comp_card))
    player_card_arr, comp_card_arr = player_card.split(), comp_card.split()
    comp_rank = check_rank(comp_card_arr[0])
    player_rank =  check_rank(player_card_arr[0])
    if (player_rank > comp_rank):
        sleep(1)
        print("Player Won the round!")
        p1.player_hand.add_to_hand(comp_card)
        p2.player_hand.remove_from_hand(comp_card)
        while (cards_on_hold):
            p1.player_hand.add_to_hand(cards_on_hold.pop())
    elif (player_rank < comp_rank):
        sleep(1)
        print("Computer Won the round!")
        p2.player_hand.add_to_hand(player_card)
        p1.player_hand.remove_from_hand(player_card)
        while (cards_on_hold):
            p2.player_hand.add_to_hand(cards_on_hold.pop())
    else:
        sleep(1)
        print("WAR, Do the round again and whoever wins the round, gets all the cards.")
        cards_on_hold.extend([player_card, comp_card])
        p1.player_hand.remove_from_hand(player_card)
        p2.player_hand.remove_from_hand(comp_card)

    if (len(p1.player_hand.cards_in_hand) == 52):
        print(p1.player_name + " Wins!\n\n\n")
        game_over = True
    elif (len(p1.player_hand.cards_in_hand) == 0):
        print(p2.player_name + " Wins!\n\n\n")
        game_over = True
    
# Use the 3 classes along with some logic to play a game of war!
