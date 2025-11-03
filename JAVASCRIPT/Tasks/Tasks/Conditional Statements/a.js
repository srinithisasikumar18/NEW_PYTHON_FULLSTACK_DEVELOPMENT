//  Write a program to check if a number is divisible by 7 or not? 

let input = require('prompt-sync')()
let num = parseInt(input("Enter the number:"))
if (num %= 7 == 0) {
    console.log("Divisible by 7")
}
else {
    console.log("Not Divisible by 7")
}
