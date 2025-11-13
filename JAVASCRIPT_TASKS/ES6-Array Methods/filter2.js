let ages = [{ name: "Sam", age: 22 },
{ name: "Eden", age: 16 }
]
let age = ages.filter((a) => {
    return a["age"] > 18
})
console.log(age)