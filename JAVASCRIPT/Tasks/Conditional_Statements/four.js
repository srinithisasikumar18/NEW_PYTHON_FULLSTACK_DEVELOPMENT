// 24. Write a program to check if a number is 3-digit numbers or not? 
const input = require('prompt-sync')();
let num = parseInt(input("Enter the number:"))
if (num > 99 && num <= 999) {
    console.log(`${num},is a three digit number`)
}
else {
    console.log(`${num},is not a three digit number`)
}
