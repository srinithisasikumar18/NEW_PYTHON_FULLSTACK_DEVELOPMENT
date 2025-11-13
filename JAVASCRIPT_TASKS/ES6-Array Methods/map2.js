enames = [{ name: "A" }, { name: "B" }]
let names = enames.map((n) => {
    return n["name"]
})
console.log(names)