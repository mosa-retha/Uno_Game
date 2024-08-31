
class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value

    def __str__(self):
        return f"{self.color} {self.value}"

    def __repr__(self):
        return f"{self.color} {self.value}"

    def __eq__(self, other):
        return self.color == other.color and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return hash((self.color, self.value))

    def validate_move(self, card):
        """Validate the move."""
        if card.color == self.color or card.value == self.value:
            return True

    def is_wild(self):
        """Check if the card is a wild card."""
        return self.color == "wild"

    def is_special(self):
        """Check if the card is a special card."""
        return self.value in ["skip", "reverse", "draw 2", "draw 4"]


