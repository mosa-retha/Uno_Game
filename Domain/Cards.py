import random

color_cards = ["red", "green", "blue", "yellow"]
wild_cards = ["draw 4", "wild"]
special_cards = ["skip", "reverse", "draw 2"]


class Cards:
    def __init__(self):
        self.deck = self.create_deck()
        self.discard_pile = []

    def create_deck(self):
        self.deck = []
        for color in color_cards:
            for i in range(2):
                for j in range(1, 10):
                    self.deck.append((color, j))
                for special in special_cards:
                    self.deck.append((color, special))
        for i in range(4):
            for wild in wild_cards:
                self.deck.append(("wild", wild))
        random.shuffle(self.deck)

        return self.deck
