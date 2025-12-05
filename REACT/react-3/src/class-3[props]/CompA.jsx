// root component of react apllication

// let CompA = () => {
//     let eid = 101;
//     let ename = "Rahul";
//     return <div>
//         <h1>
//             Component A
//         </h1>
//         <h3>Emp Id:{eid}</h3>
//         <h3>Emp Name:{ename}</h3>
//         <h4>{4 * 9}</h4>
//     </div>
// }
// export default CompA;



import React from "react"
import CompB from "./CompB";
function CompA() {
    let eid = 101;
    let ename = "Rahul"
    return <React.Fragment>
        <h2>Component A</h2>
        <p>emp_id:{eid}; emp_name:{ename}</p>
        <hr />
        <CompB props1={"GM"} props2={[1, 2, 3, 4, 5, 6]} />
        <hr />
        <CompB emp_id={eid} emp_name={ename} />
    </React.Fragment >
}
export default CompA;