// root component of react apllication

let CompA = () => {
    let eid = 101;
    let ename = "Rahul";
    return <div>
        <h1>
            Component A
        </h1>
        <h3>Emp Id:{eid}</h3>
        <h3>Emp Name:{ename}</h3>
        <h4>{4 * 9}</h4>
    </div>
}
export default CompA;