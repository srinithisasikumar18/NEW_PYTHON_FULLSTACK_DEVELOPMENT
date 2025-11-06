// this with normal function
// function greet() {
//     console.log(this)
// }
// greet()  // prints object context


//this with fat arrow function
let greet = () => {
    console.log(this)
}
greet()