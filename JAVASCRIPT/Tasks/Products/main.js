function display_products(products) {
    rows = "";
    for (let data of products) {
        rows = rows + `<tr>
                    <td>${data.id}</td>
                    <td>${data.title}</td>
                    <td>${data.price}</td>
                    <td>${data.rating}</td>
                 </tr>`;

    }
    document.getElementById('one').innerHTML = rows
}

fetch('https://dummyjson.com/products')
    .then((response) => response.json())
    .then((json) => display_products(json.products));