package Mosa.Domain;

import Mosa.Domain.Interfaces.IAttributes;

public class UnoAttributes implements IAttributes {
    private String color;
    private String value;
    private String type;

    public UnoAttributes(String color, String value) {
        super();
        this.color = color;
        this.value = value;
    }

    @Override
    public void setAttribute(String key, Object value) {

    }

    @Override
    public void getAttribute() {

    }

    @Override
    public void removeAttribute(String key) {

    }

    @Override
    public void updateAttribute(String key, Object value) {

    }

    @Override
    public void clearAttributes() {

    }

    @Override
    public void hasAttribute() {

    }

    @Override
    public void getAttributeKeys() {

    }

    @Override
    public void getAttributeValues() {

    }

    @Override
    public void getAttributeCount() {

    }

    @Override
    public void getAttributeTypes() {

    }
}
