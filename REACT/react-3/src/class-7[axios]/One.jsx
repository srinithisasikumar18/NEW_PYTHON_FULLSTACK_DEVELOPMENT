import React, { useState } from 'react'

const One = () => {
    let [state, setState] = useState("Hello");
    let updateHandler = (msg) => {
        setState(msg)
    }
    return <div>
        <h3>Message Component</h3>
        <hr />
        <h2>Message:{state}</h2>
        <button onClick={updateHandler.bind(null, "GM")}>GM</button>
        <button onClick={updateHandler.bind(null, "GA")}>GA</button>
        <button onClick={updateHandler.bind(null, "GE")}>GE</button>
        <button onClick={updateHandler.bind(null, "GN")}>GN</button>
    </div>
}
export default One