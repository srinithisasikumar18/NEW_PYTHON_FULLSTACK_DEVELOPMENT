//Normal way of doing spread
let numbers = [101, 102, 103, 104]
let eids = []
for (let num of numbers) {
    eids.push(num)
}
console.log(eids)



let number = [101, 102, 103, 104];
let index = 1;
let new_number = [];

while (index <= number.length - 1) {
    new_number.push(number[index]);
    index++;
}

console.log(new_number);