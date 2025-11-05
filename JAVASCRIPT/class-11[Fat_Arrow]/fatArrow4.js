// Using fat arrow function
let add = (a, b, c) => {
    return a + b + 1;
}
add()
add()

//if our fumction have only one return statement then no need to have {} function block as well --know as implicit return
let adds = (a, b) => a + b + 1
let r1 = adds(1, 2)
console.log(r1)