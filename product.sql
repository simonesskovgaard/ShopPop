DROP TABLE IF EXISTS Product CASCADE;

CREATE TABLE IF NOT EXISTS Product (
    pk SERIAL UNIQUE NOT NULL PRIMARY KEY,
    Category VARCHAR(30),
    Item VARCHAR(30),
    Brand VARCHAR(30),
    Size VARCHAR(10),
    Price INT
);

DELETE FROM Product;

CREATE INDEX IF NOT EXISTS product_index
ON Product (Category, Item, Brand);

DROP TABLE IF EXISTS Sell;

CREATE TABLE IF NOT EXISTS Sell (
    seller_pk INT NOT NULL REFERENCES Sellers(pk) ON DELETE CASCADE,
    product_pk INT NOT NULL REFERENCES Product(pk) ON DELETE CASCADE,
    available BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (seller_pk, product_pk)
);

CREATE INDEX IF NOT EXISTS sell_index
ON Sell (seller_pk, available);

DELETE FROM Sell;

DROP TABLE IF EXISTS ProductOrder;

CREATE TABLE IF NOT EXISTS ProductOrder (
    pk SERIAL NOT NULL PRIMARY KEY,
    customer_pk INT NOT NULL REFERENCES Customers(pk) ON DELETE CASCADE,
    seller_pk INT NOT NULL REFERENCES Sellers(pk) ON DELETE CASCADE,
    product_pk INT NOT NULL REFERENCES Product(pk) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

DELETE FROM ProductOrder;

CREATE OR REPLACE VIEW vw_product
AS
SELECT p.Category, p.Item, p.Brand,
       p.Size, p.Price, s.available,
       p.pk AS product_pk,
       S.email AS seller_name,
       S.pk AS seller_pk
FROM Product p
JOIN Sell s ON s.product_pk = p.pk
JOIN Sellers S ON s.seller_pk = S.pk
ORDER BY available, p.pk;
