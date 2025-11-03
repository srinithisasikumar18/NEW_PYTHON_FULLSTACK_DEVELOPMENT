//27. Write a program to print the least number given two numbers? 
const input = require('prompt-sync')();
let num1 = parseInt(input("Enter the first number:"))
let num2 = parseInt(input("Enter the second number:"))
if (num1 < num2) {
    console.log(`${num1},is least number`)
}
else {
    console.log(`${num2},is least number`)
}