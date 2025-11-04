//33. JS Program check if a number is divisible by 7 or not using a ternary operator? 
const input = require('prompt-sync')();
let num = parseInt(input("Enter the number:"))
num % 7 == 0 ? console.log("Divisible by Seven") : console.log("Not Divisible by Seven")