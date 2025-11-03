// 30. Write a program to print the given 3 numbers in ascending orders? 
const input = require('prompt-sync')();
let num1 = parseInt(input("Enter the first number:"))
let num2 = parseInt(input("Enter the second number:"))
let num3 = parseInt(input("Enter the third number:"))
numbers = []
numbers.push(num1)
numbers.push(num2)
numbers.push(num3)
console.log(numbers)
numbers.sort();
console.log(numbers)