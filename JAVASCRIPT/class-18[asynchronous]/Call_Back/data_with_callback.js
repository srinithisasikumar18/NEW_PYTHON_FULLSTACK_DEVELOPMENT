let employees = [{ eid: 101, ename: "Rahul", esal: 40000 },
{ eid: 102, ename: "modi", esal: 50000 }]

let createEmployee = (emp, callback) => {
    setTimeout(() => {
        employees.push(emp);
        callback()
    }, 4000)

}
console.log(employees)
let getEmployee = () => {
    setTimeout(() => {
        let rows = ""
        for (let emp of employees) {
            rows = rows + `<tr>
            <td>${emp.eid} </td>
            <td>${emp.ename} </td>
            <td>${emp.esal} </td>
            </tr>`
        }
        document.getElementById('one').innerHTML = rows
    }, 1000)

}

createEmployee({ eid: 103, ename: "priya", esal: 55000 }, getEmployee)
// getEmployee()

