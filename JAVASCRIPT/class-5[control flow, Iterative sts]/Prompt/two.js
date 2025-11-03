//WAP to find given is even or odd
//read data from users

let prompt=require('prompt-sync')()
num=parseInt(prompt("Enter the number:"))
// if (num%2==0){
//     console.log("Number is Even")
// }
// else{
//     console.log("Number is Odd")
// }
num%2==0 ? console.log("Even") : console.log("Odd")