DROP TABLE IF EXISTS Product CASCADE;

CREATE TABLE IF NOT EXISTS Product (
    pk SERIAL PRIMARY KEY,
    category VARCHAR(30),
    item VARCHAR(30),
    brand VARCHAR(30),
    size VARCHAR(10),
    price INT
);



CREATE TABLE IF NOT EXISTS Sell (
    seller_pk INT NOT NULL REFERENCES Sellers(user_id) ON DELETE CASCADE,
    product_pk INT NOT NULL REFERENCES Product(pk) ON DELETE CASCADE,
    available BOOLEAN DEFAULT TRUE,
    PRIMARY KEY (seller_pk, product_pk)
);


CREATE TABLE IF NOT EXISTS ProductOrder (
    pk SERIAL NOT NULL PRIMARY KEY,
    customer_pk INT NOT NULL REFERENCES Customers(user_id) ON DELETE CASCADE,
    seller_pk INT NOT NULL REFERENCES Sellers(user_id) ON DELETE CASCADE,
    product_pk INT NOT NULL REFERENCES Product(pk) ON DELETE CASCADE,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE INDEX IF NOT EXISTS product_index ON Product (category, item, brand);
CREATE INDEX IF NOT EXISTS sell_index ON Sell (seller_pk, available);


DELETE FROM Product;
DELETE FROM Sell;
DELETE FROM ProductOrder;


SELECT setval(pg_get_serial_sequence('Product', 'pk'), COALESCE(MAX(pk), 1) + 1, false) FROM Product;


CREATE OR REPLACE VIEW vw_product AS
SELECT p.category, p.item, p.brand,
       p.size, p.price, s.available,
       p.pk AS product_pk,
       S.email AS seller_name,
       S.user_id AS seller_pk
FROM Product p
JOIN Sell s ON s.product_pk = p.pk
JOIN Sellers S ON s.seller_pk = S.user_id
ORDER BY available, p.pk;