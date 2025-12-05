// function App() {
//     return <div>Welcome to ReactJS</div>
// }
// export default App;


//----------------------------------------------------------------------------------------------------------------------------------

// class-2
// import ReactDom from 'react-dom/client'
// import Header from './component/Header'
// let root = ReactDom.createRoot(document.getElementById('root'))
// function App() {

//     return <div>
//         <h1>App Component</h1>
//         <hr />
//         <Header />
//         <Footer />
//     </div>
// }
// export default App;


//----------------------------------------------------------------------------------------------------------------------------------


// class - 3
// import CompA from "./props/CompA"

// function App() {
//     return <div>
//         <h1>App Component</h1>
//         <hr />
//         <CompA />

//     </div>
// }
// export default App;


// import Movie from "./props/Movie";
// function App() {
//     return <div>
//         <Movie />
//     </div>
// }
// export default App;

// import Comp_B from "./props/Comp_B";
// function App() {
//     return <div>
//         <h1>App Component</h1>
//         <hr />
//         <Comp_B />

//     </div>
// }
// export default App;

// import CompA from "./class-8[]/CompA";
// let App = () => {
//     return <div>
//         {/* <h1>Styling React</h1> */}
//         <CompA />
//     </div>
// }
// export default App;

//----------------------------------------------------------------------------------------------------------------------------------


// class-4
// import React from "react";
// let App = () => {
//     return <React.Fragment>
//         <h3>App Component</h3>
//     </React.Fragment>
// }
// export default App;

// import React, { Fragment } from "react";
// let App = () => {
//     return <Fragment>
//         <h3>App Component</h3>
//     </Fragment>
// }
// export default App;



// componentA and componentB
// import React, { Fragment } from "react";
// import ComponentA from "./class-4/ComponentA";
// let App = () => {
//     return <Fragment>
//         <ComponentA />
//     </Fragment>
// }
// export default App;


// Props DRilling
// import React, {Fragment} from "react";
// import CompA from './CompA'
// import CA from "./PD/CA";
// let App=()=>{

//     return <Fragment>
//                 <h3>App Component</h3>
//                 <hr/>
//             <CA/>
//             </Fragment>
// }
// export default App;

//----------------------------------------------------------------------------------------------------------------------------------

// class-5[STATE]
// import React from "react"
// import Message from "./class-5[state]/Message"
// let App = () => {
//     return <div>
//         <h2>State</h2>
//         <Message />

//     </div>
// }
// export default App;

// import React from "react"
// import Counter from "./class-5[state]/Counter";
// let App = () => {
//     return <div>
//         <h2>State</h2>
//         <Counter />

//     </div>
// }
// export default App;


//----------------------------------------------------------------------------------------------------------------------------------
// CLASS-6
// import Message from "./class-6[Styling]/Message";
// import '../node_modules/bootstrap/dist/css/bootstrap.css'

// let App = () => {
//     return <div>
//         {/* <h1>Styling React</h1> */}
//         <Message />
//     </div>
// }
// export default App;

// NAVBAR
// import Navbar from "./class-6[Styling]/Navbar"
// import '../node_modules/bootstrap/dist/css/bootstrap.css'

// let App = () => {
//     return <div>
//         {/* <h1>Styling React</h1> */}
//         <Navbar />
//     </div>
// }
// export default App;


// //----------------------------------------------------------------------------------------------------------------------------------
// // CLASS-7
// import One from "./class-7[]/One"
// // import '../node_modules/bootstrap/dist/css/bootstrap.css'

// let App = () => {
//     return <div>
//         {/* <h1>Styling React</h1> */}
//         <One />
//     </div>
// }
// export default App;


//----------------------------------------------------------------------------------------------------------------------------------
// CLASS-8
// import Users from "./class-8[axios]/Users"
// let App = () => {
//     return <div>
//         <h3>Axios</h3>
//         <hr />
//         <Users />
//     </div>
// }
// export default App;

import UsersA from "./class-8[axios]/UsersA";
let App = () => {
    return <div>
        <h3>Axios</h3>
        <hr />
        <UsersA />
    </div>
}
export default App;