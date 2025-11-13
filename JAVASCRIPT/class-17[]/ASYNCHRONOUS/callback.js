
// with callback:::

function sum(a, b) {
    return a + b
}
function multi(a, b) {
    return a * b
}
function calc(a, b, callback) {
    return callback(a, b)
}
let r3 = calc(10, 20, sum)
let r4 = calc(10, 20, multi)
console.log(r3)
console.log(r4)