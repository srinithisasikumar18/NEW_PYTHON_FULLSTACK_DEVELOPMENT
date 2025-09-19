 CREATE table bunit(
 b_Id int ,
 name varchar(32),
 loc varchar(32),
 PRIMARY KEY(b_Id)
 );
    
	
INSERT INTO bunit(
VALUES
(1001,'ATT','NY'),
(1002,'COLT','london'),
(1003,'ARITEL','mumbai'),
(1004,'JIO','nvida');

CREATE TABLE empl(
eid int,
ename varchar(32) NOT NULL,
esal float NOT NULL,
bu_Id int,
age int check(age>18),
PRIMARY KEY(eid),
FOREIGN KEY(bu_Id) REFERENCES bunit(b_Id)
);


INSERT INTO empl
VALUES
(101,"rg",45000.00,1003,45),
(102,"sg",55000.00,1004,35),
(103,"pg",65000.09,1003,65);



INSERT INTO empl
VALUES
(101,'Rahul',45000,1003,45);


INSERT INTO empl
VALUES
(102,'Sonia',45000,1003,75);


INSERT INTO empl
VALUES
(103,'Priyanka',65000,1003,42);