

class Dealer:
    def __init__(self, players, cards):
        super().__init__()
        self.deck = cards.deck
        self.discard_pile = cards.discard_pile
        self.players = players

    def deal_cards(self):
        """Deal cards to players."""
        for player in self.players:
            for _ in range(7):
                player.add_players_card(self.deck.pop())
        self.discard_pile.append(self.deck.pop())
