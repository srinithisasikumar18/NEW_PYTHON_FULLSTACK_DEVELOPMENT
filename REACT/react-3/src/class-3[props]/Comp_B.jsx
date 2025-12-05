// root component of react apllication
import CompB from "./CompB";
let Comp_B = () => {
    let eid = 101;
    let ename = "Rahul";
    return <div>
        <h1>
            Component A
        </h1>
        <hr />
        {/* <CompB msg={"Good Morning"} eid={eid} ename={ename} /> */}
        <CompB msg={"Good Morning"} />

    </div>
}
export default Comp_B;