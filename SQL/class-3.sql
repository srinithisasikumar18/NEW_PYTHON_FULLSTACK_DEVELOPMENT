OPERATORS IN SQL:
* like--invloves wildcard OPERATOR
%-matches one or more CHARACTERs
_-matches exactly only one charcater
ex: "R%" starts with R and followed by any no of charcaters

CREATE TABLE employee(
eid int,
ename varchar(32),
esal float,
loc varchar(32)
);
INSERT INTO employee
VALUES
(101,"Rahul",45000.09,"HYD"),
(102,"sonia",55000.09,"CHN"),
(103,"priyanka",65000.09,"BNG"),
(104,"rajini",75000.09,"ND"),
(105,"modi",65000.09,"HYD"),
(106,"Vijay",85000.09,"CHN"),
(108,"virat",195000.09,"BNG"),
(109,"rohit",185000.09,"MUM"),
(110,"Rahul",15000.09,"BNG");
INSERT INTO employee
VALUE
(107,"hardik",78989.09,"MUM");

1)write a query to fetch all employees their name dtart with "R"
select  *
from employee
where ename like "R%";
+------+--------+---------+------+
| eid  | ename  | esal    | loc  |
+------+--------+---------+------+
|  101 | Rahul  | 45000.1 | HYD  |
|  104 | rajini | 75000.1 | ND   |
|  109 | rohit  |  185000 | MUM  |
|  110 | Rahul  | 15000.1 | BNG  |
+------+--------+---------+------+

2)ends with "i"
select *
from employee
where ename like "%i";
+------+--------+---------+------+
| eid  | ename  | esal    | loc  |
+------+--------+---------+------+
|  104 | rajini | 75000.1 | ND   |
|  105 | modi   | 65000.1 | HYD  |
+------+--------+---------+------+

3)3rd CHARACTER with "j"
select *
from employee
where ename like "__j%";
+------+--------+---------+------+
| eid  | ename  | esal    | loc  |
+------+--------+---------+------+
|  104 | rajini | 75000.1 | ND   |
|  106 | Vijay  | 85000.1 | CHN  |
+------+--------+---------+------+

4)max esal
select * from employee
where esal=(select max(esal) from employee);
