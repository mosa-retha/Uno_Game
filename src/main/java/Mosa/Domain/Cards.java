package Mosa.Domain;

import Mosa.Domain.Interfaces.ICards;

public class Cards implements ICards {
    private String color;
    private String value;
    private String type;

    public Cards(String color, String value) {
        super();
        this.color = color;
        this.value = value;
    }


    public Cards() {
        super();
    }


    @Override
    public String toString() {
        return "Cards{" +
                "color='" + color + '\'' +
                ", value='" + value + '\'' +
                '}';
    }

    @Override
    public void setCardColor(String color) {
        this.color = color;
    }

    @Override
    public String getCardColor() {
        return "";
    }

    @Override
    public void setCardValue(int value) {
        this.value = String.valueOf(value);

    }

    @Override
    public int getCardValue() {
        return 0;
    }

    @Override
    public void setCardType(String type) {
        this.type = type;

    }

    @Override
    public String getCardType() {
        return "";
    }
}
