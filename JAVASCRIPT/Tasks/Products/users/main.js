function display_users(users) {
    rows = "";
    for (let user of users) {
        rows = rows + `<tr>
        <td>${user.id}</td>
        <td>${user.name}</td>
        <td>${user.gender}</td>
        <td>${user.address.city}</td>
        </tr>`
    }
    document.getElementById('one').innerHTML = rows
}
fetch('https://jsonplaceholder.typicode.com/users')
    .then((response) => response.json())
    .then((json) => display_users(json));



// let users = fetch("https://jsonplaceholder.typicode.com/users")