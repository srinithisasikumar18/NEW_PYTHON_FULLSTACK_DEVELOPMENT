// for every element a new element with another array is created
let enames = ["rahul", "priya", "modi", "gandhi"]
let users = enames.map((names) => {
    return names.toUpperCase()
})
console.log(users)
