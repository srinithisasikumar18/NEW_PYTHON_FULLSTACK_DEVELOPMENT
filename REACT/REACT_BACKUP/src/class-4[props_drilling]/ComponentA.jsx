// import ComponentB from "./ComponentB";
// let wish = () => {
//     return "Good Morning"
// }
// let ComponentA = () => {
//     let eid = 101;
//     let employees = [{ "eid": 1, "ename": "Had", "gender": "Male" },
//     { "eid": 2, "ename": "Lyn", "gender": "Male" },
//     { "eid": 3, "ename": "Bert", "gender": "Male" },
//     { "eid": 4, "ename": "Hiram", "gender": "Non-binary" },
//     { "eid": 5, "ename": "Gui", "gender": "Female" },
//     { "eid": 6, "ename": "Raeann", "gender": "Agender" },
//     { "eid": 7, "ename": "Sybila", "gender": "Female" },
//     { "eid": 8, "ename": "Carmon", "gender": "Female" },
//     { "eid": 9, "ename": "Any", "gender": "Male" },
//     { "eid": 10, "ename": "Giana", "gender": "Female" }]
//     return <div>
//         <h2>Component A</h2>
//         <h3>{wish()}</h3>
//         <hr />
//         <ComponentB greet={wish} emp_Id={eid} employees={employees} />
//         {/* <ComponentB /> */}

//     </div>
// }
// export default ComponentA;


// CONDITIONAL STATEMENTS

import ComponentB from "./ComponentB";
let wish = () => {
    return "Good Morning"
}
let ComponentA = () => {
    let eid = 101;
    let employees = [{ "eid": 1, "ename": "Had", "gender": "Male" },
    { "eid": 2, "ename": "Lyn", "gender": "Male" },
    { "eid": 3, "ename": "Bert", "gender": "Male" },
    { "eid": 4, "ename": "Hiram", "gender": "Non-binary" },
    { "eid": 5, "ename": "Gui", "gender": "Female" },
    { "eid": 6, "ename": "Raeann", "gender": "Agender" },
    { "eid": 7, "ename": "Sybila", "gender": "Female" },
    { "eid": 8, "ename": "Carmon", "gender": "Female" },
    { "eid": 9, "ename": "Any", "gender": "Male" },
    { "eid": 10, "ename": "Giana", "gender": "Female" }]
    return <div>
        <h2>Component A</h2>
        <h3>{wish()}</h3>
        <hr />
        <h4>{1 ? <p>GA</p> : <p>GN</p>}</h4>
        <ComponentB greet={wish} emp_Id={eid} employees={employees} />
    </div>
}
export default ComponentA;