introduction to sql using CRUD operations:
creating a table:
create table employee(
    -> eid int,
    -> ename varchar(32),
    -> esal float
    -> );
inserting values at a time:
insert into employee
     values
    (101,"rahul",45000.00),
    (102,"srinithi",56000.67),
	(103,"kokila",45678.09);
to read:
select * from table;
inserting values one at a time:
> insert into employee
    ->      values
    -> (104,"sasi",678989.98);