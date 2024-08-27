
class Player:
    def __init__(self, name):
        self.name = name
        self.players_cards = []

    def add_players_card(self, card):
        self.players_cards.append(card)

    def players_cards(self):
        return self.players_cards
