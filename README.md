# ShopPop

ShopPop is an interactive web-app for online shopping. 
Users can create an account and list products, which are added to the database to be viewed by other users.

To run ShopPop:
1. Create a database called 'shoppop' using port 5433

CREATE DATABASE shoppop;


2. Create a user called 'shop' with password 'pop'
CREATE USER shop WITH PASSWORD 'pop';

3. Grant all privileges to user 
GRANT ALL PRIVILEGES ON DATABASE shoppop TO shop;

4. Create environment and install requirements.txt
pip install -r requirements.txt

5. Upload users.sql and product.sql to database using command:

psql -U shop -d shoppop -h localhost -p 5433 -f /path/to/file

6. Upload fashion data to database using command:

\copy Product(item,brand,category,price,size) FROM /path/to/fp.csv DELIMITER ',' CSV HEADER;

7. run app using command 'python app.py' 

8. register user and log in

9. Shop til you drop!
