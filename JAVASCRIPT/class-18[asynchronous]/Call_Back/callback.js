function greet(name, callback) {
    console.log("hello" + name)
    callback()
}
greet("rahul", () => {
    console.log("welcome")
})