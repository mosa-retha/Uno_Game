import random

from Domain.Card import Card

color_cards = ["red", "green", "blue", "yellow"]
wild_cards = ["draw 4", "wild"]
special_cards = ["skip", "reverse", "draw 2"]


class Deck(Card):
    def __init__(self, color="", value=""):
        super().__init__(color, value)
        self.deck = self.create_deck()
        self.discard_pile = []




    def create_deck(self):
        """Create a deck of cards."""
        self.deck = []
        for color in color_cards:
            for i in range(2):
                for j in range(1, 10):
                    self.deck.append(Card(color, str(j)))
                for special in special_cards:
                    self.deck.append(Card(color, special))
        for i in range(4):
            for wild in wild_cards:
                self.deck.append(Card("wild", wild))
        random.shuffle(self.deck)

        return self.deck
