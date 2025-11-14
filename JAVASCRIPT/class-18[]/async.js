console.time("execution time")
console.log("R1")
console.log("R2")
console.log("R3")
console.log("R4")
console.timeEnd("execution time")


console.time("execution time")
setTimeout(() => { console.log("R1") }, 5000)
setTimeout(() => { console.log("R2") }, 1000)
setTimeout(() => { console.log("R3") }, 7000)
setTimeout(() => { console.log("R4") }, 1000)
console.timeEnd("execution time")



