// function App() {
//     return <div>Welcome to ReactJS</div>
// }
// export default App;



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
import React, { Fragment } from "react";
import ComponentA from "./class-4/ComponentA";
let App = () => {
    return <Fragment>
        <ComponentA />
    </Fragment>
}
export default App;