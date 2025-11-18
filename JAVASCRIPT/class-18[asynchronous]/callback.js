function sum(a, b) {
    return a + b
}
function mnulti(a, b) {
    return a * b
}
function cal(a, b, callback) {
    return callback(a, b)
}
let r1 = cal(10, 20, sum)
console.log(r1)