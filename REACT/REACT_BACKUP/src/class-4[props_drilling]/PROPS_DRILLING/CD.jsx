let CD = (props) => {

    return <div>
        <h4>Component D</h4>
        <pre>{JSON.stringify(props)}</pre>
        <h3>Message:{props.data}</h3>
    </div>
}
export default CD;