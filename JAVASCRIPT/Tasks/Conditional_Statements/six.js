//26. Write a program to print the greatest number in given two numbers? 
const input = require('prompt-sync')();
let num1 = parseInt(input("Enter the first number:"))
let num2 = parseInt(input("Enter the second number:"))
if (num1 > num2) {
    console.log(`${num1}, is greatest number`)
}
else {
    console.log(`${num2}, is greatest number`)
}