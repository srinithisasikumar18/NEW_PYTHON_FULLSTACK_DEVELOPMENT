function cal() {
    let numbers = [10, 20, 25, 30, 45]
    for (let nums of numbers) {
        if (nums % 2 !== 0) {
            return;
        }
        console.log(nums)
    }
    console.log("good morning")
}
cal()


//if break::10 20 good morning
//if return::
// function cal() {
//     let number = [2, 4, 133, 5, 3, 20, 30]
//     for (let num of number) {
//         console.log(num)
//         if (num % 2 == 0)

//             return
//     }
// }
// cal()