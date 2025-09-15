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