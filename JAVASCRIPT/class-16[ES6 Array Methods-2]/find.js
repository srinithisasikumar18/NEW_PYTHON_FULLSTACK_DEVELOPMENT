let employee = [
    { eid: 101, ename: "Rahul" },
    { eid: 102, ename: "priya" },
    { eid: 103, ename: "modi" }
]
let emp = employee.find((emp) => {
    return emp.eid === 103;
})
console.log(emp)