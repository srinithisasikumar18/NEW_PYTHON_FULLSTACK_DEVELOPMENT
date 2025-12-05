// import { useState } from "react";


// let Message = () => {
//     // let msg = "Hello"
//     let [msg, setMsg] = useState("Hello.....");
//     let gmHandler = () => {
//         setMsg("Good Morning")
//     }
//     let gnHandler = () => {
//         setMsg("Good Night")
//     }
//     let gaHandler = () => {
//         setMsg("Good Afternoon")
//     }
//     let resetHandler = () => {
//         setMsg("Hello.....")
//     }
//     return <div>
//         <h3>Message Component</h3>
//         <hr />
//         <h4>Message:{msg}</h4>
//         <hr />
//         <button onClick={gmHandler}>GM</button>
//         <button onClick={gaHandler}>GA</button>
//         <button onClick={gnHandler}>GN</button>
//         <button onClick={resetHandler}>Reset</button>

//     </div>
// }
// export default Message;


// WITHOUT EVENT HANDLERS

import { useState } from "react";

let Message = () => {
    // let msg = "Hello"
    let [msg, setMsg] = useState("Hello.....");
    // let gmHandler = () => {
    //     setMsg("Good Morning")
    // }
    // let gnHandler = () => {
    //     setMsg("Good Night")
    // }
    // let gaHandler = () => {
    //     setMsg("Good Afternoon")
    // }
    // let resetHandler = () => {
    //     setMsg("Hello.....")
    // }
    return <div>
        <h3>Message Component</h3>
        <hr />
        <h4>Message:{msg}</h4>
        <hr />
        <button onClick={() => { setMsg("Good Morning") }}>GM</button>
        <button onClick={() => { setMsg("Good Afternoon") }}>GA</button>
        <button onClick={() => { setMsg("Good Night") }}>GN</button>
        <button onClick={() => { setMsg("Hello....") }}>Reset</button>

    </div>
}
export default Message; 