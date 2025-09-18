introduction to sql using CRUD operations:
CREATING:
creating a table:
create table employee(
     eid int,
     ename varchar(32),
     esal float
     );
inserting values at a time:
insert into employee
     values
    (101,"rahul",45000.00),
    (102,"srinithi",56000.67),
	(103,"kokila",45678.09);
	
READING:	
to read:
select * from table;

inserting values one at a time:
> insert into employee
    ->      values
    -> (104,"sasi",678989.98);
DELETING:
deleting all the rows:
 delete from employee;
to delete selected columns:
delete from employee
where eid=104;

UPDATING:
UPDATE employee
set ename="srinithi"
where eid=102;
