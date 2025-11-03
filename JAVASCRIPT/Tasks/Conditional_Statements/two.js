// 22. Write a program to check if a number is multiple of 3 or not? 
const input = require('prompt-sync')()
let num = parseInt(input(("Enter the Number")))
if (num % 3 == 0) {

    console.log(`${num} is a multiple of 3`);
} else {
    console.log(`${num} is not a multiple of 3`);
}