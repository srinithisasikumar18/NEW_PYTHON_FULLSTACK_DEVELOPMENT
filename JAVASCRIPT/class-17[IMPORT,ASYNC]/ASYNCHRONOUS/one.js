// synchronous:---disadvantage of it is blocking others requests
// asynchronous:---executing muiltiple request at a time
// at the time of executing statements in asynchronous there will be some problems hence we use ---- callback, promise, await , async
// callback-- passing function as a arguement
// without callback::
function calc(a, b, op) {
    if (op === "sum") {
        return a + b
    }
    if (op === "multi") {
        return a * b
    }
}
let r1 = calc(10, 20, "sum")
console.log(r1)
let r2 = calc(10, 20, "multi")
console.log(r2)


