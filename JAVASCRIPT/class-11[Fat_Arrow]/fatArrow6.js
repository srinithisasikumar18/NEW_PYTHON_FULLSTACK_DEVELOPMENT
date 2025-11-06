// function wish() {
//     console.log("hi")
// }
// wish()
// function wish() {
//     console.log("i")
// }
// wish()
// i i


// overriding---function hoisting
// function hoisting and variable hoisting
var wish = () => {
    console.log("hi")
}
wish()
var wish = () => {
    console.log("bye")
}
wish()