create table customer(
    -> cid int,
    -> cname varchar(32),
    -> corders varchar(32),
    -> PRIMARY KEY(cid)
    -> );
insert into customer
    -> values
    -> (101,"srinithi","iphone"),
    -> (102,"kokila","samsungs"),
    -> (103,"deepa","onplus t");
+-----+----------+----------+
| cid | cname    | corders  |
+-----+----------+----------+
| 101 | srinithi | iphone   |
| 102 | kokila   | samsungs |
| 103 | deepa    | onplus t |
+-----+----------+----------+

create table customer_orders(
     ord_id int,
     ord_name varchar(32),
     cu_id int,
     price float,
     PRIMARY KEY(ord_id),
     FOREIGN KEY(cu_id) REFERENCES customer(cid)
     );
insert into customer_orders
    -> values
    -> (1001,'phone',101,56789.09),
    -> (1002,'phone',101,126789.09),
    -> (1003,'phone',103,46789.09);
+--------+----------+-------+---------+
| ord_id | ord_name | cu_id | price   |
+--------+----------+-------+---------+
|   1001 | phone    |   101 | 56789.1 |
|   1002 | phone    |   101 |  126789 |
|   1003 | phone    |   103 | 46789.1 |
+--------+----------+-------+---------+

QUERY:
> select
    -> customer.cname,
    -> customer_orders.ord_name
    -> from
    -> customer,
    -> customer_orders
    -> where customer.cid=customer_orders.cu_id;
OUTPUT:
+----------+----------+
| cname    | ord_name |
+----------+----------+
| srinithi | phone    |
| srinithi | phone    |
| deepa    | phone    |
+----------+----------+