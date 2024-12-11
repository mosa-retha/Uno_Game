package Mosa.Domain;

import java.util.List;

public class Deck extends Cards {
    private int deckSize;
    private int deckCount;
    private List<Cards> discardPile;

    public Deck() {
        super();
    }

    public Deck(int deckSize, int deckCount) {
        super();
        this.deckSize = deckSize;
        this.deckCount = deckCount;
    }

    public int getDeckSize() {
        return deckSize;
    }

    public void setDeckSize(int deckSize) {
        this.deckSize = deckSize;
    }

    public int getDeckCount() {
        return deckCount;
    }

    public void createDeck() {
        System.out.println("Deck created");
    }

    @Override
    public String toString() {
        return "Deck{" +
                "deckSize=" + deckSize +
                ", deckCount=" + deckCount +
                '}';
    }
}
