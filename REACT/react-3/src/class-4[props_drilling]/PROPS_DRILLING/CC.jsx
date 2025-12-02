import CD from "./CD";
let CC = (props) => {

    return <div>
        <h4>Component C</h4>
        <pre>{JSON.stringify(props)}</pre>
        <hr />
        <CD data={props.data} />
    </div>
}
export default CC;