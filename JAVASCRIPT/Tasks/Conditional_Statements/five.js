//25. Write a program to print even or odd for a given number
const input = require('prompt-sync')();
let num = parseInt(input("Enter the number:"))
if (num % 2 == 0) {
    console.log("Even")
}
else {
    console.log("Odd")
}