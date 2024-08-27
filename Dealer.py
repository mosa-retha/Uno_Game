import random

color_cards = ["red", "green", "blue", "yellow"]
wild_cards = ["draw 4", "wild"]
special_cards = ["skip", "reverse", "draw 2"]
used_cards = {}


def dealt(card_colour, card_value):
    try:
        if len(used_cards) == 0:
            used_cards[card_colour] = []
            used_cards[card_colour].append(card_value)
            return False
        else:
            used_cards[card_colour].append(card_value)
    except KeyError:
        used_cards[card_colour] = [card_value]
    finally:
        return True


def deal_card():
    card_colour = random.choice(color_cards)
    card_value = random.randint(0, 14)
    if card_value == 0:
        card_value = wild_cards[random.randint(0, 1)]
    elif card_value > 9:
        card_value = special_cards[card_value - 10]

    if dealt(card_colour, card_value):
        return card_colour, card_value
    else:
        return deal_card()
