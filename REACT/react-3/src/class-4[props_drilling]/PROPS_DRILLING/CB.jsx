import CB from './CB'
let CA = () => {
    let data = "GM";
    return <div>
        <h4>Component A</h4>
        <hr />
        <CB data={data} />
    </div>
}
export default CA;