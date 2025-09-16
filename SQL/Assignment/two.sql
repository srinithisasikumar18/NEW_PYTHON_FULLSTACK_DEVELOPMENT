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

create table customer_orders(
     ord_id int,
     ord_name varchar(32),
     cu_id int,
     price float,
     PRIMARY KEY(ord_id),
     FOREIGN KEY(cu_id) REFERENCES customer(cid)
     );
	 
(1001,'phone',101,56789.09),
(1002,'phone',101,126789.09),
(1003,'phone',103,46789.09);