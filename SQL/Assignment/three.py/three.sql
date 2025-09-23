create table employees (
eid INT ,
fname VARCHAR(32),
lname VARCHAR(32),
city VARCHAR(32),
esal INT,
age INT,
PRIMARY KEY(eid)
);
insert into employees values
(101,'Rahul','Gandhi','Wayanad',45000,52),
(102,'Sonia','Gandhi','New Delhi',55000,75),
(103,'Priyanka','Gandhi','Nodia',65000,45),
(104,'Modi','Narendra','New Delhi',75000,69),
(105,'Rajni','Kanth','Chennai',85000,65),
(106,'Vijay','Setupathi','Chennai',95000,47),
(107,'Nayana','Tara','Chennai',25000,40),
(108,'Alia','Bhut','Mumbai',45000,31),
(109,'Mahesh','Bhut','Mumbai',15000,68),
(110,'Sonam','Kapoor','Mumbai',30000,27),
(111,'Anil','Kapoor','Mumbai',38000,40),
(112,'Raj','Kapoor','Mumbai',18000,78),
(113,'Vishnu','Manchu','Hyderabad',10000,40),
(114,'Manoj','Manchu','Hyderabad',12000,35);
INSERT INTO employees (eid,fname,lname,city,age)
values
(115,'Mohan','Manchu','Hyderabad',70);
=======================================================================
select * from employees;
+-----+----------+-----------+-----------+-------+------+
| eid | fname    | lname     | city      | esal  | age  |
+-----+----------+-----------+-----------+-------+------+
| 101 | Rahul    | Gandhi    | Wayanad   | 45000 |   52 |
| 102 | Sonia    | Gandhi    | New Delhi | 55000 |   75 |
| 103 | Priyanka | Gandhi    | Nodia     | 65000 |   45 |
| 104 | Modi     | Narendra  | New Delhi | 75000 |   69 |
| 105 | Rajni    | Kanth     | Chennai   | 85000 |   65 |
| 106 | Vijay    | Setupathi | Chennai   | 95000 |   47 |
| 107 | Nayana   | Tara      | Chennai   | 25000 |   40 |
| 108 | Alia     | Bhut      | Mumbai    | 45000 |   31 |
| 109 | Mahesh   | Bhut      | Mumbai    | 15000 |   68 |
| 110 | Sonam    | Kapoor    | Mumbai    | 30000 |   27 |
| 111 | Anil     | Kapoor    | Mumbai    | 38000 |   40 |
| 112 | Raj      | Kapoor    | Mumbai    | 18000 |   78 |
| 113 | Vishnu   | Manchu    | Hyderabad | 10000 |   40 |
| 114 | Manoj    | Manchu    | Hyderabad | 12000 |   35 |
| 115 | Mohan    | Manchu    | Hyderabad |  NULL |   70 |
+-----+----------+-----------+-----------+-------+------+

Assignments
--------------------------------------------------------------
1. Write a query to fetch employee whose last name is same.
SELECT *
FROM
employees
WHERE lname='Gandhi'
	OR lname='Bhut'
	OR lname='Kapoor'
	OR lname='Manchu';
OUTPUT:
+-----+----------+--------+-----------+-------+------+
| eid | fname    | lname  | city      | esal  | age  |
+-----+----------+--------+-----------+-------+------+
| 101 | Rahul    | Gandhi | Wayanad   | 45000 |   52 |
| 102 | Sonia    | Gandhi | New Delhi | 55000 |   75 |
| 103 | Priyanka | Gandhi | Nodia     | 65000 |   45 |
| 108 | Alia     | Bhut   | Mumbai    | 45000 |   31 |
| 109 | Mahesh   | Bhut   | Mumbai    | 15000 |   68 |
| 110 | Sonam    | Kapoor | Mumbai    | 30000 |   27 |
| 111 | Anil     | Kapoor | Mumbai    | 38000 |   40 |
| 112 | Raj      | Kapoor | Mumbai    | 18000 |   78 |
| 113 | Vishnu   | Manchu | Hyderabad | 10000 |   40 |
| 114 | Manoj    | Manchu | Hyderabad | 12000 |   35 |
| 115 | Mohan    | Manchu | Hyderabad |  NULL |   70 |
+-----+----------+--------+-----------+-------+------+


2. Write a query to fetch whose age is grater then 70.
SELECT *
FROM employees
WHERE age>=70;
OUTPUT:
+-----+-------+--------+-----------+-------+------+
| eid | fname | lname  | city      | esal  | age  |
+-----+-------+--------+-----------+-------+------+
| 102 | Sonia | Gandhi | New Delhi | 55000 |   75 |
| 112 | Raj   | Kapoor | Mumbai    | 18000 |   78 |
| 115 | Mohan | Manchu | Hyderabad |  NULL |   70 |
+-----+-------+--------+-----------+-------+------+


3. Write a query to fetch employee with same city.
SELECT *,
employees.fname
FROM
employees
WHERE city='New Delhi'
	OR city='Mumbai'
	OR city='Chennai'
	OR city='Hyderabad';
OUTPUT:
+-----+--------+-----------+-----------+-------+------+--------+
| eid | fname  | lname     | city      | esal  | age  | fname  |
+-----+--------+-----------+-----------+-------+------+--------+
| 102 | Sonia  | Gandhi    | New Delhi | 55000 |   75 | Sonia  |
| 104 | Modi   | Narendra  | New Delhi | 75000 |   69 | Modi   |
| 105 | Rajni  | Kanth     | Chennai   | 85000 |   65 | Rajni  |
| 106 | Vijay  | Setupathi | Chennai   | 95000 |   47 | Vijay  |
| 107 | Nayana | Tara      | Chennai   | 25000 |   40 | Nayana |
| 108 | Alia   | Bhut      | Mumbai    | 45000 |   31 | Alia   |
| 109 | Mahesh | Bhut      | Mumbai    | 15000 |   68 | Mahesh |
| 110 | Sonam  | Kapoor    | Mumbai    | 30000 |   27 | Sonam  |
| 111 | Anil   | Kapoor    | Mumbai    | 38000 |   40 | Anil   |
| 112 | Raj    | Kapoor    | Mumbai    | 18000 |   78 | Raj    |
| 113 | Vishnu | Manchu    | Hyderabad | 10000 |   40 | Vishnu |
| 114 | Manoj  | Manchu    | Hyderabad | 12000 |   35 | Manoj  |
| 115 | Mohan  | Manchu    | Hyderabad |  NULL |   70 | Mohan  |
+-----+--------+-----------+-----------+-------+------+--------+


4. Write a query to fetch whose name ends with 'h'.
select *
FROM employees
where lname LIKE '%h';
OUTPUT:
+-----+-------+-------+---------+-------+------+
| eid | fname | lname | city    | esal  | age  |
+-----+-------+-------+---------+-------+------+
| 105 | Rajni | Kanth | Chennai | 85000 |   65 |
+-----+-------+-------+---------+-------+------+


5. Write a query to count employee whose last name ends with 'i'.
select count(*) AS 'Last name with i'
FROM employees
where lname LIKE '%i';
OUTPUT:
+------------------+
| Last name with i |
+------------------+
|                4 |
+------------------+


6. Write a query to find employee with highest salary.
select max(esal) AS 'highest sal'
from employees;
OUTPUT:
+-------------+
| highest sal |
+-------------+
|       95000 |
+-------------+


7. Write a query to find employee with lowest salary.
select min(esal) AS 'lowest sal'
from employees;
OUTPUT:
+------------+
| lowest sal |
+------------+
|      10000 |
+------------+


8. Write a query to change last name of employee whose id is 102.
UPDATE employees
SET lname='Sharma'
where eid=102;
OUTPUT:
+-----+----------+-----------+-----------+-------+------+
| eid | fname    | lname     | city      | esal  | age  |
+-----+----------+-----------+-----------+-------+------+
| 101 | Rahul    | Gandhi    | Wayanad   | 45000 |   52 |
| 102 | Sonia    | Sharma    | New Delhi | 55000 |   75 |
| 103 | Priyanka | Gandhi    | Nodia     | 65000 |   45 |
| 104 | Modi     | Narendra  | New Delhi | 75000 |   69 |
| 105 | Rajni    | Kanth     | Chennai   | 85000 |   65 |
| 106 | Vijay    | Setupathi | Chennai   | 95000 |   47 |
| 107 | Nayana   | Tara      | Chennai   | 25000 |   40 |
| 108 | Alia     | Bhut      | Mumbai    | 45000 |   31 |
| 109 | Mahesh   | Bhut      | Mumbai    | 15000 |   68 |
| 110 | Sonam    | Kapoor    | Mumbai    | 30000 |   27 |
| 111 | Anil     | Kapoor    | Mumbai    | 38000 |   40 |
| 112 | Raj      | Kapoor    | Mumbai    | 18000 |   78 |
| 113 | Vishnu   | Manchu    | Hyderabad | 10000 |   40 |
| 114 | Manoj    | Manchu    | Hyderabad | 12000 |   35 |
| 115 | Mohan    | Manchu    | Hyderabad |  NULL |   70 |
+-----+----------+-----------+-----------+-------+------+


9. Write a query to find name of employee whose name start's with 'A' and city name starts with 'B''.
select 
employees.fname,
employees.city
from
employees
where fname like 'A%'
   and city like 'B%';
OUTPUT:
Empty set (0.00 sec)


10. Write a query to find employee with highest salary in 'Bangalore'.
select max(esal) AS 'highest sal'
from employees
where city='Bangalore';
OUTPUT:
+-------------+
| highest sal |
+-------------+
|        NULL |
+-------------+


11. Write a query to find employee who live in 'Hyderabad' with age above 70.
select *
from employees
where city='Hyderabad' 
	  AND age>=70;
OUTPUT:
+-----+-------+--------+-----------+------+------+
| eid | fname | lname  | city      | esal | age  |
+-----+-------+--------+-----------+------+------+
| 115 | Mohan | Manchu | Hyderabad | NULL |   70 |
+-----+-------+--------+-----------+------+------+


12. Write a query to find employee with salary below 50000.
select *
from employees
where esal<=50000;
OUTPUT:
+-----+--------+--------+-----------+-------+------+
| eid | fname  | lname  | city      | esal  | age  |
+-----+--------+--------+-----------+-------+------+
| 101 | Rahul  | Gandhi | Wayanad   | 45000 |   52 |
| 107 | Nayana | Tara   | Chennai   | 25000 |   40 |
| 108 | Alia   | Bhut   | Mumbai    | 45000 |   31 |
| 109 | Mahesh | Bhut   | Mumbai    | 15000 |   68 |
| 110 | Sonam  | Kapoor | Mumbai    | 30000 |   27 |
| 111 | Anil   | Kapoor | Mumbai    | 38000 |   40 |
| 112 | Raj    | Kapoor | Mumbai    | 18000 |   78 |
| 113 | Vishnu | Manchu | Hyderabad | 10000 |   40 |
| 114 | Manoj  | Manchu | Hyderabad | 12000 |   35 |
+-----+--------+--------+-----------+-------+------+


13. Write a query to find name of employee with salary range between 20000 to 40000.
SELECT fname, esal
FROM employees
WHERE esal BETWEEN 20000 AND 40000;
       (or)
SELECT fname, esal
FROM employees
WHERE esal >= 20000
  AND esal <= 40000;
OUTPUT:
+--------+-------+
| fname  | esal  |
+--------+-------+
| Nayana | 25000 |
| Sonam  | 30000 |
| Anil   | 38000 |
| Vishnu | 20000 |
+--------+-------+


15. Write a query to find employee whose first name third character is 'j'.
select *
FROM employees
where fname LIKE '__j%';
OUTPUT:
+-----+-------+-----------+---------+-------+------+
| eid | fname | lname     | city    | esal  | age  |
+-----+-------+-----------+---------+-------+------+
| 105 | Rajni | Kanth     | Chennai | 85000 |   65 |
| 106 | Vijay | Setupathi | Chennai | 95000 |   47 |
| 112 | Raj   | Kapoor    | Mumbai  | 18000 |   78 |
+-----+-------+-----------+---------+-------+------+


16. Write a query to find employee whose first name third character is 'j' and live in 'Bangalore'.
select *
FROM employees
where fname LIKE '__j%'
	and city='Bangalore';
OUTPUT:
Empty set (0.00 sec)


17. Write a query to count employees whose first name third character is 'j'.
select count(*) AS 'emp with j'
FROM employees
where fname LIKE '__j%';
OUTPUT:
+------------+
| emp with j |
+------------+
|          3 |
+------------+


18. Write a query to fetch employee with lowest salary and add 10000 to its salary.
select eid
from employees
where esal=(SELECT min(esal) from employees);
UPDATE employees
set esal=esal+10000
where eid=113;
OUTPUT:
+-----+----------+-----------+-----------+-------+------+
| eid | fname    | lname     | city      | esal  | age  |
+-----+----------+-----------+-----------+-------+------+
| 101 | Rahul    | Gandhi    | Wayanad   | 45000 |   52 |
| 102 | Sonia    | Sharma    | New Delhi | 55000 |   75 |
| 103 | Priyanka | Gandhi    | Nodia     | 65000 |   45 |
| 104 | Modi     | Narendra  | New Delhi | 75000 |   69 |
| 105 | Rajni    | Kanth     | Chennai   | 85000 |   65 |
| 106 | Vijay    | Setupathi | Chennai   | 95000 |   47 |
| 107 | Nayana   | Tara      | Chennai   | 25000 |   40 |
| 108 | Alia     | Bhut      | Mumbai    | 45000 |   31 |
| 109 | Mahesh   | Bhut      | Mumbai    | 15000 |   68 |
| 110 | Sonam    | Kapoor    | Mumbai    | 30000 |   27 |
| 111 | Anil     | Kapoor    | Mumbai    | 38000 |   40 |
| 112 | Raj      | Kapoor    | Mumbai    | 18000 |   78 |
| 113 | Vishnu   | Manchu    | Hyderabad | 20000 |   40 |
| 114 | Manoj    | Manchu    | Hyderabad | 12000 |   35 |
| 115 | Mohan    | Manchu    | Hyderabad |  NULL |   70 |
+-----+----------+-----------+-----------+-------+------+


19. Write a query to Sort the table by ascending.
"with esalary"
select * 
from employees
ORDER by esal ;
OUTPUT:
+-----+----------+-----------+-----------+-------+------+
| eid | fname    | lname     | city      | esal  | age  |
+-----+----------+-----------+-----------+-------+------+
| 115 | Mohan    | Manchu    | Hyderabad |  NULL |   70 |
| 114 | Manoj    | Manchu    | Hyderabad | 12000 |   35 |
| 109 | Mahesh   | Bhut      | Mumbai    | 15000 |   68 |
| 112 | Raj      | Kapoor    | Mumbai    | 18000 |   78 |
| 113 | Vishnu   | Manchu    | Hyderabad | 20000 |   40 |
| 107 | Nayana   | Tara      | Chennai   | 25000 |   40 |
| 110 | Sonam    | Kapoor    | Mumbai    | 30000 |   27 |
| 111 | Anil     | Kapoor    | Mumbai    | 38000 |   40 |
| 101 | Rahul    | Gandhi    | Wayanad   | 45000 |   52 |
| 108 | Alia     | Bhut      | Mumbai    | 45000 |   31 |
| 102 | Sonia    | Sharma    | New Delhi | 55000 |   75 |
| 103 | Priyanka | Gandhi    | Nodia     | 65000 |   45 |
| 104 | Modi     | Narendra  | New Delhi | 75000 |   69 |
| 105 | Rajni    | Kanth     | Chennai   | 85000 |   65 |
| 106 | Vijay    | Setupathi | Chennai   | 95000 |   47 |
+-----+----------+-----------+-----------+-------+------+


20. Write a query to Sort the table by descending.
select * 
from employees
ORDER by esal DESC;
OUTPUT:
+-----+----------+-----------+-----------+-------+------+
| eid | fname    | lname     | city      | esal  | age  |
+-----+----------+-----------+-----------+-------+------+
| 106 | Vijay    | Setupathi | Chennai   | 95000 |   47 |
| 105 | Rajni    | Kanth     | Chennai   | 85000 |   65 |
| 104 | Modi     | Narendra  | New Delhi | 75000 |   69 |
| 103 | Priyanka | Gandhi    | Nodia     | 65000 |   45 |
| 102 | Sonia    | Sharma    | New Delhi | 55000 |   75 |
| 101 | Rahul    | Gandhi    | Wayanad   | 45000 |   52 |
| 108 | Alia     | Bhut      | Mumbai    | 45000 |   31 |
| 111 | Anil     | Kapoor    | Mumbai    | 38000 |   40 |
| 110 | Sonam    | Kapoor    | Mumbai    | 30000 |   27 |
| 107 | Nayana   | Tara      | Chennai   | 25000 |   40 |
| 113 | Vishnu   | Manchu    | Hyderabad | 20000 |   40 |
| 112 | Raj      | Kapoor    | Mumbai    | 18000 |   78 |
| 109 | Mahesh   | Bhut      | Mumbai    | 15000 |   68 |
| 114 | Manoj    | Manchu    | Hyderabad | 12000 |   35 |
| 115 | Mohan    | Manchu    | Hyderabad |  NULL |   70 |
+-----+----------+-----------+-----------+-------+------+


21. Write a query to show employee whose name's last third word is 'j'' and salary is more then 30000. 
select *
FROM employees
where fname LIKE '__j%'
	and esal>30000;
OUTPUT:
+-----+-------+-----------+---------+-------+------+
| eid | fname | lname     | city    | esal  | age  |
+-----+-------+-----------+---------+-------+------+
| 105 | Rajni | Kanth     | Chennai | 85000 |   65 |
| 106 | Vijay | Setupathi | Chennai | 95000 |   47 |
+-----+-------+-----------+---------+-------+------+


22. Write a query to show all employee who live in 'Bangalore' and 'Wayanad'.
select * 
from employees
where city="Bangalore" 
	or city="Wayanad";
OUTPUT:
+-----+-------+--------+---------+-------+------+
| eid | fname | lname  | city    | esal  | age  |
+-----+-------+--------+---------+-------+------+
| 101 | Rahul | Gandhi | Wayanad | 45000 |   52 |
+-----+-------+--------+---------+-------+------+


23. Write a query to fetch employee with first name count is 5.
select * 
from employees
where LENGTH(fname)=5;
OUTPUT:
+-----+-------+-----------+-----------+-------+------+
| eid | fname | lname     | city      | esal  | age  |
+-----+-------+-----------+-----------+-------+------+
| 101 | Rahul | Gandhi    | Wayanad   | 45000 |   52 |
| 102 | Sonia | Sharma    | New Delhi | 55000 |   75 |
| 105 | Rajni | Kanth     | Chennai   | 85000 |   65 |
| 106 | Vijay | Setupathi | Chennai   | 95000 |   47 |
| 110 | Sonam | Kapoor    | Mumbai    | 30000 |   27 |
| 114 | Manoj | Manchu    | Hyderabad | 12000 |   35 |
| 115 | Mohan | Manchu    | Hyderabad |  NULL |   70 |
+-----+-------+-----------+-----------+-------+------+


24. Write a query to group by employee with their age.
select age,fname
from employees
group by age,fname;
OUTPUT:
+------+----------+
| age  | fname    |
+------+----------+
|   52 | Rahul    |
|   75 | Sonia    |
|   45 | Priyanka |
|   69 | Modi     |
|   65 | Rajni    |
|   47 | Vijay    |
|   40 | Nayana   |
|   31 | Alia     |
|   68 | Mahesh   |
|   27 | Sonam    |
|   40 | Anil     |
|   78 | Raj      |
|   40 | Vishnu   |
|   35 | Manoj    |
|   70 | Mohan    |
+------+----------+


26. Write a query to find employee with null salary.
select *
from employees
where esal is NULL;
OUTPUT:
+-----+-------+--------+-----------+------+------+
| eid | fname | lname  | city      | esal | age  |
+-----+-------+--------+-----------+------+------+
| 115 | Mohan | Manchu | Hyderabad | NULL |   70 |
+-----+-------+--------+-----------+------+------+