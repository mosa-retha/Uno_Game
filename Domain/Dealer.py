

class Dealer:
    def __init__(self, players, cards):
        super().__init__()
        self.deck = cards
        self.players = players

    def create_deck(self):
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
        self.discard_pile.append(self.deck.pop())

    def deal_card(self):
        for player in self.players:
            for _ in range(7):
                player.players_cards().append(self.deck[0])
                self.discard_pile.append(self.deck.pop())
            
        

