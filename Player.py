import threading
import time


class Player(threading.Thread):
    def __init__(self):
        self.players_cards = []

    def run(self):
        for i in range(5):
            print(f"Running in thread: {i}")
            time.sleep(1)

    def players_cards(self, cards):
        self.players_cards = cards
