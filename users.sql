DROP TABLE IF EXISTS Users CASCADE;

CREATE TABLE IF NOT EXISTS Users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL
);


CREATE INDEX IF NOT EXISTS users_index
ON Users (user_id, username);

DELETE FROM Users;

DROP TABLE IF EXISTS Sellers CASCADE;

CREATE TABLE IF NOT EXISTS Sellers(
    PRIMARY KEY(user_id)
) INHERITS (Users);

CREATE INDEX IF NOT EXISTS sellers_index
ON Sellers (user_id, username);

DELETE FROM Sellers;

INSERT INTO Sellers(username, email, password)
VALUES ('seller', 'Seller', 'pass');

DROP TABLE IF EXISTS Customers;

CREATE TABLE IF NOT EXISTS Customers(
    PRIMARY KEY(user_id)
) INHERITS (Users);

CREATE INDEX IF NOT EXISTS customers_index
ON Customers (user_id, username);

DELETE FROM Customers;

INSERT INTO Customers(username, email, password)
VALUES ('customer', 'Customer', 'pass');