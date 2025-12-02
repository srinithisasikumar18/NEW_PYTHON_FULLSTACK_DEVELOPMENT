import { useState } from "react";

let Counter = () => {
    let [counter, setCounter] = useState(1);
    let incrHandler = () => {
        setCounter(counter + 1)
    }
    let decrHandler = () => {
        setCounter(counter - 1)
    }

    return <div>
        <h4>Counter Example</h4>
        <hr />
        <h3>Count:{counter}</h3>
        <hr />
        {/* <button onClick={() => { setCounter(counter + 1) }}>+</button>              WITHOUT HANDLERS
        <button onClick={() => { setCounter(counter - 1) }}>-</button> */}
        <button onClick={incrHandler}>+</button>
        <button onClick={decrHandler}>-</button>
    </div>
}
export default Counter;