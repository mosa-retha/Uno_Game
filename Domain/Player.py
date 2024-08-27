
class Player:
    def __init__(self, name):
        self.name = name
        self.players_cards = []

    def add_players_card(self, card):
        """Add a card to the player's hand."""
        self.players_cards.append(card)

    def players_cards(self):
        """Return the player's cards."""
        return self.players_cards
