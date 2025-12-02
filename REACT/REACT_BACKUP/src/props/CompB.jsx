let CompB = (props) => {
    return <div>
        <h1>
            Component B
        </h1>
        <pre>{JSON.stringify(props)}</pre>
        <h1>Employee_Id:{props.eid}</h1>
        <h1>Employee_Name:{props.ename}</h1>
    </div>
}
export default CompB;