//filter values based on the condition
let enames = ["rahul", "priya", "modi", "gandhi", "srinithi"]
let new_emp = enames.filter((names) => {
    return names.length >= 5;
})
console.log(new_emp)

let names = enames.filter(nam => nam.length >= 5)
console.log(names)


let number = [11, 7, 8, 232, 1055, 41, 8, 12]
// let even_num = []
// for (let num of number) {
//     if (num % 2 == 0) {
//         even_num.push(num)
//     }
// }
// console.log(even_num)

// let even_num = number.filter((num) => {
//     return num % 2 == 0;
// })
// console.log(even_num)

// we can able to convert the above code into one line if return is there then we can you implicit 
let nums = number.filter(num => num % 2 == 0)
console.log(nums)