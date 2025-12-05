import ReactDOM from 'react-dom/client'
import App from './App';
// import '../node_modules/bootstrap/dist/css/bootstrap.css'
let root = ReactDOM.createRoot(document.getElementById('root'))
//root.render("GM")
//root.render(<h1>Good Morning</h1>);
// root.render(<h1>GM</h1><h2>GA</h2>)
// root.render(<><h1>GM</h1><h2>GA</h2></>)
// root.render(<div><h1>GM</h1><h2>GA</h2></div>)
root.render(<App />)

