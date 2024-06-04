DROP TABLE IF EXISTS Users CASCADE;

-- CREATE TABLE IF NOT EXISTS Sellers (
--     pk SERIAL PRIMARY KEY,
--     email VARCHAR(100) UNIQUE NOT NULL,
--     full_name VARCHAR(100) NOT NULL,
--     password VARCHAR(200) NOT NULL
-- );

-- CREATE TABLE IF NOT EXISTS Product (
--     pk SERIAL UNIQUE NOT NULL PRIMARY KEY,
--     Category VARCHAR(30),
--     Item VARCHAR(30),
--     Brand VARCHAR(30),
--     Size VARCHAR(10),
--     Price INT
-- );


CREATE TABLE IF NOT EXISTS Users (
    pk SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    password VARCHAR(200) NOT NULL
);


CREATE INDEX IF NOT EXISTS users_index
ON Users (pk, username);

DELETE FROM Users;

DROP TABLE IF EXISTS Sellers CASCADE;

CREATE TABLE IF NOT EXISTS Sellers(
    PRIMARY KEY(pk)
) INHERITS (Users);

CREATE INDEX IF NOT EXISTS sellers_index
ON Sellers (pk, username);

DELETE FROM Sellers;

INSERT INTO Sellers(username, email, password)
VALUES ('seller', 'Seller', 'pass');

DROP TABLE IF EXISTS Customers;

CREATE TABLE IF NOT EXISTS Customers(
    PRIMARY KEY(pk)
) INHERITS (Users);

CREATE INDEX IF NOT EXISTS customers_index
ON Customers (pk, username);

DELETE FROM Customers;

INSERT INTO Customers(username, email, password)
VALUES ('customer', 'Customer', 'pass');