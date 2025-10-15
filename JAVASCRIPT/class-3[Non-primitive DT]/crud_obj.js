var a={}
var emp={
    "eid":101,
    "ename":"srinithi",
    "easl":45000.50
}

// READ

console.log(emp)
console.log(a)
console.log(typeof a)
console.log(typeof emp)
console.log(emp.eid)
console.log(emp.ename)

// UPDATE

emp.esal=50000.50;
console.log(emp)
emp.gender="Female";
console.log(emp)

// DELETE
delete emp.eid
console.log(emp)