var users;
async function display_user() {
    // let t_body = document.getElementById("one")
    // console.log(t_body)
    users = await fetch("https://jsonplaceholder.typicode.com/users")
        .then((resp) => { return resp.json() })
        .then((data) => { return data })
        .catch(() => { })
    rows = "";
    for (let user of users) {
        rows = rows + `<tr>
            <td>${user.id}</td>
            <td>${user.name}</td>
            <td>${user.email}</td>
            </tr>`
    }
    document.getElementById("one").innerHTML = rows

}
display_user();