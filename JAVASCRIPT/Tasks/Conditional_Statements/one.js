const input = require('prompt-sync')()
let num = parseInt(input(("Enter the Number")))
if (num % 7 == 0) {
    console.log("Divisible by 7")
}
else {
    console.log("Not Divisible by 7")
}