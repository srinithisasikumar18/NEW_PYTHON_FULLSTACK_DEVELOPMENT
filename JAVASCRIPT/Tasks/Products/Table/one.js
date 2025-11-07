function display_users(users) {
    males = "";
    females = "";
    other = "";
    for (let user of users) {
        if (user["gender"] === "male") {
            males = males + `<tr>
            <td>${user.id}</td>
            <td>${user.firstName}</td>
            <td>${user.gender}</td>
        </tr>`}
        else if (user["gender"] === "female") {
            females = females + `<tr>
            <td>${user.id}</td>
            <td>${user.firstName}</td>
            <td>${user.gender}</td>
        </tr>`}

        else {
            other = other + `<tr>
            <td>${user.id}</td>
            <td>${user.firstName}</td>
            <td>${user.gender}</td>
        </tr>`}
    }
    document.getElementById('one').innerHTML = males;
    document.getElementById('two').innerHTML = females;
    document.getElementById('three').innerHTML = other;

}



fetch('https://dummyjson.com/users')
    .then((response) => response.json())
    .then((json) => display_users(json.users));