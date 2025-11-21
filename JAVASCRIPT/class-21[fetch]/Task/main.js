// function display_user() {
//     rows = "";
//     for (let product of prod) {
//         rows = rows + `<tr>
//             <td>${product.id}</td>
//             <td>${product.title}</td>
//             <td>${product.price}</td>
//             <td>${product.rating}</td>
//             </tr>`
//     }
//     document.getElementById("one").innerHTML = rows

// }

// fetch("https://dummyjson.com/products")
//     .then((resp) => resp.json())
//     .then((data) => {
//         prod = data.products; // IMPORTANT
//         display_user();
//     })
//     .catch((err) => { document.getElementById("one").innerHTML = "no data" })
//     ;



let display_Products = () => {
    fetch('https://dummyjson.com/products')
        .then((resp) => { return resp.json() })
        .then((product_data) => {
            let rows = ""
            for (product of product_data.products) {
                rows = rows + `<tr>
                            <td>${product.id}</td>
                            <td>${product.title}</td>
                            <td>${product.price}</td>
                            <td>${product.rating}</td>
                       </tr>`
            }
            document.getElementById('one').innerHTML = rows
        })
        .catch((err) => {
            document.getElementById('one').innerHTML = "No Data"
        })



}

display_Products()




const display_Productss = async () => {
    const tb = document.querySelector("tbody");

    try {
        const resp = await fetch("https://dummyjson.com/products");
        const data = await resp.json();

        const rows = data.products.map(product => `
            <tr>
                <td>${product.id}</td>
                <td>${product.title}</td>
                <td>${product.price}</td>
                <td>${product.rating}</td>
            </tr>
        `).join("");

        tb.innerHTML = rows;

    } catch (error) {
        tb.innerHTML = "<tr><td colspan='4'>No Data</td></tr>";
    }
};

display_Productss();