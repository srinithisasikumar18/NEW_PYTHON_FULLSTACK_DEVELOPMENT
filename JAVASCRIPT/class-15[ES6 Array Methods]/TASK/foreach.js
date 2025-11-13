let enames = ["rahul", "priya", "sonia", "modi"]
// enames.forEach(function () {
//     console.log("gm")
// })
// enames.forEach(ename => { console.log(ename) })
// function names() {
//     forEach(names in enames)
//     console.log(names)

// }
// names()

let users = enames.forEach((ename) => {
    // console.log(ename)
    return ename.toUpperCase()
})
console.log(users)      //undefined