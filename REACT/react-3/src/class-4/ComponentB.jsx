import React from 'react'

const ComponentB = (props) => {
    let { greet, emp_Id } = props;  //Object Destructuring
    return (
        <div>
            <h3>Component B</h3>
            <h3>{JSON.stringify(props)}</h3>
            <h4>{greet()}</h4>
            <h4>{emp_Id}</h4>
            <table border={2}>
                <thead>
                    <th>ID</th>
                    <th>NAME</th>
                    <th>GENDER</th>
                </thead>

                <tbody>
                    {
                        props.employees.map((emp) => {
                            return <tr>
                                <td>{emp.eid}</td>
                                <td>{emp.ename}</td>
                                <td>{emp.gender}</td>
                            </tr>
                        })
                    }
                </tbody>
            </table>
        </div>
    )
}
export default ComponentB;