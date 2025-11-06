// Using fat arrow function
var add = (a, b) => {
    return a + b + 1;
}
let r = add(10, 10)
console.log(r)
let rr = add(20, 10)
console.log(rr)

//if our fumction have only one return statement then no need to have {} function block as well --know as implicit return
var add = (a, b) => a + b + 1
let r1 = add(1, 2)
console.log(r1)