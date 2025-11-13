let emp = {
    eid: 101,
    ename: "rahul",
    details: {
        email: "rahulga@gmail.com",
        loc: "wayand"
    }
}
console.log(emp.ename)
console.log(emp.details.loc)


//object destructing
let { ename, details } = emp;
let { loc } = details
console.log(loc);
