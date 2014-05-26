from enum import Enum
import random
class Suit(Enum):
    Spade = "S"
    Heart = "H"
    Club = "C"
    Diamond = "D"
    
class Value(Enum):    
    Two = "2"
    Three = "3"
    Four = "4"
    Five = "5"
    Six = "6"
    Seven = "7"
    Eight = "8"
    Nine = "9"
    Jack = "J"
    Queen = "Q"
    King = "K"
    Ace = "A"
    

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    def __repr__(self):
        return self.suit.name + "-" + self.value.name
    
    def __str__(self):
        return self.suit.name + "-" + self.value.name
        
class Deck:
    
    cards = []
    
    def __init__(self):
        for suit in Suit:
            for value in Value:
                self.cards.append(Card(value, suit))
                
    def shuffle(self):
        #using Knuth algorithm for shuffling
        sizeOfDeck = len(self.cards)
        i = sizeOfDeck
        while i > 0:
            i = i -1
            randomCardIndex = random.randint(0, sizeOfDeck - 1)
            card = self.cards[randomCardIndex]
            self.cards[randomCardIndex] = self.cards[i]
            self.cards[i] = card
            
    def add_card(self, card):
        self.cards.append(card)
    
    def deal_card(self, hand):
        hand.add_card(self.cards.pop())
            
    def __repr__(self):
        stringForm = ""
        for card in self.cards:
           stringForm = stringForm + "\n" + str(card)
        return stringForm

class Hand:
    cards = []
    
    def __init__(self):
        pass
    
    def add_card(self, card):
        self.cards.append(card)
    
    def return_card(self, deck):
        deck.add_card(self.cards.pop())
    
    def __repr__(self):
        stringForm = ""
        for card in self.cards:
           stringForm = stringForm + "\n" + str(card)
        return stringForm
        