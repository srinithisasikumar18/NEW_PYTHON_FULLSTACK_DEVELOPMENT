cmd>mysql -uroot -proot

system cls;
show databases;
CREATE DATABASE dbone;

USE dbone;

show tables;

CREATE TABLE employees();

CREATE TABLE employees(
eid int,
ename VARCHAR(32), 
esal  float
);

DESC employees


SELECT *FROM employees;


INSERT INTO employees
VALUES
(101,'Rahul',45000.45);
===============================
class-2

mysql -uroot -proot

system cls;

CREATE DATABASE dbtwo;

USE dbtwo;
CREATE TABLE employees();


CREATE TABLE employees(
eid int,
ename VARCHAR(32),
esal FLOAT,
loc VARCHAR(32)
);

DESC employees;


mysql> DESC employees;
+-------+-------------+------+-----+---------+-------+
| Field | Type        | Null | Key | Default | Extra |
+-------+-------------+------+-----+---------+-------+
| eid   | int         | YES  |     | NULL    |       |
| ename | varchar(32) | YES  |     | NULL    |       |
| esal  | float       | YES  |     | NULL    |       |
| loc   | varchar(32) | YES  |     | NULL    |       |
+-------+-------------+------+-----+---------+-------+
4 rows in set (0.03 sec)


SELECT *FROM employees;

INSERT INTO employees
VALUES
(101,'Rahul',45000.45,'Wayanad');

INSERT INTO employees
VALUES
(102,'Sonia',55000.55,'New Delhi'),
(103,'Priyanka',65000.65,'New Delhi');

INSERT INTO employees(eid,ename,loc)
VALUES
(104,'Modi','Bangalore');

INSERT INTO employees(eid,ename)
VALUES
(105,'Amith');


UPDATE employees
SET ename="Rahul Gandhi JI"
WHERE eid=101;

UPDATE employees
SET esal=400;


DELETE FROM employees
WHERE eid=105;

DELETE FROM employees;

=================================
mysql -uroot -proot
system cls;

show databases;
USE dbtwo;
show tables;

CREATE TABLE employees(
eid int,
ename VARCHAR(32),
esal float,
loc VARCHAR(32)
);
DESC employees;

SELECT eid,ename 
FROM employees;

SELECT eid AS Employee_Id,
       ename AS Name,
	   loc AS Location
FROM employees;


SELECT eid AS "Employee Id",
       ename AS Name,
	   loc AS Location
FROM employees;
==========================================
CONSTRAINT ON mysql ? rules ON data
NOT NULL      -  NULL VALUES NOT allowed,but duplicate allowed
UNIQUE        -  duplicates are NOT allowed but NULL VALUES allowed
CHECK
DEFAULT 
PRIMARY KEY  - NOT NULL +UNIQUE 
FOREIGN KEY 
INDEX

DROP TABLE employees;

CREATE TABLE employees(
eid INT UNIQUE,
ename VARCHAR(32) NOT NULL,
esal  float,
age  int,
loc VARCHAR(32) DEFAULT 'Bangalore'
);

DESC employees;

INSERT INTO employees
VALUES
(101,'Rahul',45000.45,46,'Wayanad');

INSERT INTO employees(ename,esal,age,loc)
VALUES
('Sonia',55000.55,80,'New Delhi');

INSERT INTO employees(eid,esal,age,loc)
VALUES
(103,75000.75,71,'New Delhi');

INSERT INTO employees(eid,ename,esal,age)
VALUES
(104,'Modi',75000,78);



INSERT INTO employees(eid,ename,esal,age)
VALUES
(105,'Rajni',85000,8);

=====================================
DROP TABLE employees;


CREATE TABLE employees(
eid INT UNIQUE,
ename VARCHAR(32) NOT NULL,
esal float,
age INT CHECK(age>=18),
loc VARCHAR(32) DEFAULT 'Bangalore'
);

DESC employees;
INSERT INTO employees
VALUES
(105,'Rajni',85000,8,'Chennai');