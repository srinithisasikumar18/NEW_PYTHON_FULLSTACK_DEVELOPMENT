SELECT syntax:
SELECT * FROM
table1,table2
[WHERE]---conditions
[ORDER BY]----ordering in ascending or decending order
[GROUP BY]----grouping result rows


==================================================================================================
customers:
CREATE TABLE customers(
c_Id int,
c_name varchar(32) NOT NULL,
c_loc varchar(32) DEFAULT 'BNG',
PRIMARY KEY(c_Id)
);
INSERT into customers
VALUES
(101,'RG','BNG'),
(102,'Modi','BNG'),
(103,'SG','kl'),
(104,'PG','kl');

orders:
CREATE TABLE orders(
o_Id int,
o_Details varchar(32),
o_price float NOT NULL,
c_Id int,
o_status varchar(32)DEFAULT 'open',
PRIMARY KEY(o_Id),
FOREIGN KEY(c_Id) REFERENCES customers(c_Id)
);
INSERT INTO orders
VALUES
(10001,'MP',4567.00,101,'open'),
(10002,'MOUSE',4567.00,103,'delivered'),
(10003,'Pen',4567.00,104,'open'),
(10004,'book',4567.00,102,'open'),
(10005,'phone',456.00,102,'open'),
(10006,'dress',4507.00,103,'delivered'),
(10007,'laptop',4567.00,101,'open'),
(10008,'head phones',467.00,104,'delivered'),
(10009,'bluetooth',4567.00,101,'open'),
(10010,'glasses',456.00,102,'open'),
(10011,'vessels',4567.00,101,'open'),
(10012,'towel',45.00,102,'delivered'),
(10013,'hair dryer',4567.00,104,'open'),
(10014,'straightener',567.00,104,'open'),
(10015,'jean',456.00,103,'delivered'),
(10016,'shirts',456.00,103,'open'),
(10017,'laptop',456.00,103,'open'),
(10018,'iphone',456.00,103,'delivered'),
(10019,'jean',456.00,103,'open'),
(10020,'t-shirt',457.00,102,'open');

1)fetch all the customers
select c_Id AS "customer_id",
       c_name AS "name",
       c_loc AS "location"
from customers;
+-------------+------+----------+
| customer_id | name | location |
+-------------+------+----------+
|         101 | RG   | BNG      |
|         102 | Modi | BNG      |
|         103 | SG   | kl       |
|         104 | PG   | BNG      |
+-------------+------+----------+

2)fetch all the customers belong to BNG
select * from customers
WHERE c_loc='BNG';
+------+--------+-------+
| c_Id | c_name | c_loc |
+------+--------+-------+
|  101 | RG     | BNG   |
|  102 | Modi   | BNG   |
|  104 | PG     | BNG   |
+------+--------+-------+

3)write SQL query - display NO OF orders?
select count(*)
     from orders;
+----------+
| count(*) |
+----------+
|       20 |
+----------+
	 
4)write sql query TO FETCH customer name,ORDER name AND price
FROM customers,orders table?
 select
     customers.c_name,
     orders.o_Details,
     orders.o_price
     from
     customers ,
	 orders
	 WHERE customers.c_Id=orders.c_Id;
	 
	 (or)
select
     c.c_name AS "customer-name",
     o.o_Details as "order_details",
     o.o_price as "price"
     from
     customers c ,
	 orders o
	 WHERE c.c_Id=o.c_Id;	 
+---------------+---------------+-------+
| customer-name | order_details | price |
+---------------+---------------+-------+
| RG            | MP            |  4567 |
| RG            | dress         |  4567 |
| RG            | laptop        |  4567 |
| RG            | bluetooth     |  4567 |
| RG            | vessels       |  4567 |
| Modi          | book          |  4567 |
| Modi          | phone         |  4567 |
| Modi          | glasses       |   456 |
| Modi          | towel         |    45 |
| Modi          | t-shirt       |   457 |
| Modi          | t-shirt       |   457 |
| SG            | MOUSE         |  4567 |
| SG            | jean          |   456 |
| SG            | laptop        |   456 |
| SG            | iphone        |   456 |
| SG            | jean          |   456 |
| PG            | Pen           |  4567 |
| PG            | head phones   |   467 |
| PG            | hair dryer    |  4567 |
| PG            | straightener  |   567 |
+---------------+---------------+-------+
