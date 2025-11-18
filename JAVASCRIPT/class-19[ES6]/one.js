// if any function returns Promise then will go with .then and .catch
// .then represents success
// .catch represents failure
let employee = [
    { eid: 101, ename: "rahul" },
    { eid: 102, ename: "sonia" }
]
let createEmployee = (emp) => {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            let flag = true;
            if (flag) {
                resolve("data inserted")
                employee.push(emp)
            }
            else {
                reject("failed")
            }
        }, 4000)
    })
}
let getEmployee = () => {
    setTimeout(() => {
        let rows = "";
        for (let emp of employee) {
            rows = rows + `<tr>
            <td>${emp.eid}</td>
            <td>${emp.ename}</td>
            </tr>`
        }
        document.getElementById("one").innerHTML = rows;
    }, 1000)

}
createEmployee({ eid: 103, ename: "priya" })
    .then((msg) => {
        console.log(msg)
        getEmployee()
    })
    .catch((err) => {
        console.log(err)
    })
