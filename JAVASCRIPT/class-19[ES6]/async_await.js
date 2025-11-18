let employee = [
    { eid: 101, ename: "rahul" },
    { eid: 102, ename: "priyaa" }
]
let createEmployee = ((emp) => {
    return ((reslove, reject) => {
        let flag = true;
        if (flag) {
            reslove("data inserted")
        }
        else {
            reject("failed")
        }
    })
})
let getEmployee = () => {
    setTimeout(() => {
        rows = "";
        rows += `<tr>
    <td>${emp.eid}</td>
    <td>${emp.ename}</td>
    </tr>`
        document.getElementById("one").innerHTML = rows;
    }, 1000)

}
let exe = async () => {
    await createEmployee({ eid: 103, ename: "sonia" })
    getEmployee()
}




