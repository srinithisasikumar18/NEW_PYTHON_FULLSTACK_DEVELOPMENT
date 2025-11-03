// 23. Write a program to check if a number is positive or not? 
const input = require('prompt-sync')();
let num = parseInt(input("Enter the number"))
if (num == 0) {
    console.log("Neither Positive nor Negative")
}
else if (num > 0) {
    console.log("Positive Number")
}
else {
    console.log("Negative Number")
}