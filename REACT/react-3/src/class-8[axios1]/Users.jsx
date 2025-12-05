// import Axios from "axios"
// import { useState } from "react"
// import { Fragment } from "react"

// let Users = () => {
//     let [users, setUsers] = useState("click button to get data")
//     let getData = () => {
//         Axios.get('https://jsonplaceholder.typicode.com/users')
//             .then((resp) => { setUsers(resp.data) })
//             .catch((err) => { console.log(err) })
//     }
//     return <Fragment>
//         <button onClick={getData}>GET DATA</button>
//         <pre>{JSON.stringify(users)}</pre>
//     </Fragment>
// }
// export default Users;


// import Axios from "axios"
// import { useState } from "react"
// import { Fragment } from "react"

// let Users = () => {
//     let [users, setUsers] = useState([])
//     let getData = () => {
//         Axios.get('https://jsonplaceholder.typicode.com/users')
//             .then((resp) => { setUsers(resp.data) })
//             .catch((err) => { console.log(err) })
//     }
//     return <Fragment>
//         <button onClick={getData}>GET DATA</button>
//         <pre>{JSON.stringify(users)}</pre>
//         <table border="2">
//             <thead>
//                 <tr>
//                     <th>U_Id</th>
//                     <th>U_Name</th>
//                     <th>U_Email</th>
//                     <th>U_City</th>
//                 </tr>
//             </thead>
//             <tbody>
//                 {users.map((user) => {
//                     return <tr>
//                         <td>{user.id}</td>
//                         <td>{user.username}</td>
//                         <td>{user.email}</td>
//                         <td>{user.address.city}</td>
//                     </tr>
//                 })}
//             </tbody>
//         </table>
//     </Fragment>
// }
// export default Users;



import Axios from "axios"
import { useState } from "react"
import { Fragment } from "react"

let Users = () => {
    let [users, setUsers] = useState([])
    let getData = () => {
        Axios.get('https://jsonplaceholder.typicode.com/users')
            .then((resp) => { setUsers(resp.data) })
            .catch((err) => { console.log(err) })
    }
    return <Fragment>
        <button onClick={getData}>GET DATA</button>
        <pre>{JSON.stringify(users)}</pre>
        <table border="2">
            <thead>
                <tr>
                    <th>U_Id</th>
                    <th>U_Name</th>
                    <th>U_Email</th>
                    <th>U_City</th>
                </tr>
            </thead>
            <tbody>
                {users.map((user) => {
                    return <tr key={user.id}>
                        <td>{user.id}</td>
                        <td>{user.username}</td>
                        <td>{user.email}</td>
                        <td>{user.address.city}</td>
                    </tr>
                })}
            </tbody>
        </table>
    </Fragment>
}
export default Users;