import CC from "./CC";
let CB = (props) => {

    return <div>
        <h4>Component B</h4>
        <pre>{JSON.stringify(props)}</pre>
        <hr />
        <CC data={props.data} />
    </div>
}
export default CB;  