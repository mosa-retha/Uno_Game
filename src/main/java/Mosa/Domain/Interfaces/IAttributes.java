package Mosa.Domain.Interfaces;

public interface IAttributes {

    void setAttribute(String key, Object value);
    void getAttribute();
    void removeAttribute(String key);
    void updateAttribute(String key, Object value);
    void clearAttributes();
    void hasAttribute();
    void getAttributeKeys();
    void getAttributeValues();
    void getAttributeCount();
    void getAttributeTypes();
}
