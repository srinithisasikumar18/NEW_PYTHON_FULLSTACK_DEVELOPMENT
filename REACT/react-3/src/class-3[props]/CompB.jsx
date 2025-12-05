// let CompB = (props) => {
//     return <div>
//         <h1>
//             Component B
//         </h1>
//         <pre>{JSON.stringify(props)}</pre>
//         <h1>Employee_Id:{props.eid}</h1>
//         <h1>Employee_Name:{props.ename}</h1>
//     </div>
// }
// export default CompB;


import React from "react"
function CompB(props) {

    return <React.Fragment>
        <h2>Component B</h2>
        <pre>{JSON.stringify(props)}</pre>
        {/* <h3>Wish Message:{props.props1}</h3>
        <h3>Array:{props.props2}</h3> */}
        <h3>emp_Id:{props.emp_id} emp_Name:{props.emp_name}</h3>

    </React.Fragment>
}
export default CompB;