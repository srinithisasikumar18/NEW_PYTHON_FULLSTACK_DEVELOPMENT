joins:retreving data from one or more TABLes that includes NULL values as well.
1)find customer and their placed order details
inner join:matched records from both tables


2)
left join:



3)
right join:



create DATABASE joins;
use joins;
create table customers(
c_Id int,
c_name varchar(32) not null,
c_loc varchar(32) ,
PRIMARY KEY(c_Id)
);
INSERT INTO customers
VALUES
(101,'Rahul','wayanad'),
(102,'Sonia','Amethi'),
(103,'Priya','Amethi'),
(104,'Amith','New Delhi'),
(105,'Modi','New Delhi');

create table orders(
o_Id int,
o_details varchar(32) not null,
o_amount int,
c_Id int,
status varchar(32) DEFAULT "open",
PRIMARY KEY(o_Id),
FOREIGN KEY (c_Id) REFERENCES customers(c_Id)
);
INSERT INTO orders
VALUES
(10001,'Water Bottle',199,101,'delivered'),
(10002,'Marker Pen',299,101,'delivered'),
(10003,'Lenovo Mouse',399,101,'delivered'),
(10004,'Parker Pen',499,101,'delivered'),
(10005,'OG Movie',599,101,'delivered');

INSERT INTO orders
VALUES
(10006,'MedX Tablets',799,102,'In-Progress'),
(10007,'Bata sandles',899,102,'In-Progress');

INSERT INTO orders
VALUES
(10008,'Tata Cha',99,103,'In-Progress'),
(10009,'Water Bottles',199,103,'In-Progress'),
(10010,'Sandles',299,103,'In-Progress');
INSERT INTO orders
VALUES
(10011,'Pen -1',99,104,'Open'),
(10012,'Pen -2',199,104,'Open'),
(10013,'Pen -3',299,104,'Open'),
(10014,'Pen - 4',299,104,'Open'),
(10015,'Rolex Watch',1111299,104,'In-Progress');



select * from
customers as c,orders as o
where c.c_Id=o.c_Id;
----15 rows without Modi bcoz he is not placing any order

write a query to fetch data from both tables
cartersian: getting all the data from both tables
select * from
customers,orders;
-----75 rows 

inner join:
select * from
customers INNER JOIN orders
ON customers.c_Id=orders.c_Id;

select * from
orders INNER JOIN customers
ON orders.c_Id=customers.c_Id;

left join:it also gives Modi who hasn't placed any orders'
select * from
customers left join orders
ON customers.c_Id=orders.c_Id;

right join"