// let numbers = [234, 45, 6, 7, 89, 56, 32]

/* function num(a, b) {
    return a - b;
}
console.log(num(8, 2))
num() */
// let num = numbers.sort((a, b) => {
//     // return b - a;
//     return a-b;
// })
// console.log(num)


let number = [2, 3, 4, 6, 7, 3, 3, 2, 4, 2]
// let new_num = new Set(number)
// console.log(new_num)

let new_num = [...new Set(number)]
console.log(new_num)
