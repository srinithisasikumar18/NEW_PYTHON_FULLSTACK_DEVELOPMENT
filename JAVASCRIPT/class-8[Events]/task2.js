//how to verify given array is empty or not

let emps={}
let user={
    eid:101,
    ename:"rahul"
}
console.log(emps.length)   //length property is not present in objects so it will return undefined

console.log(user.eid)
console.log(user.ename)
console.log(Object.keys(user))
console.log(Object.keys(user).length)
console.log(Object.keys(emps).length)
emp_len=Object.keys(emps).length
user_len=Object.keys(user).length
emp_len>0 ? console.log("not empty") : console.log("empty")
user_len>0 ? console.log("not empty") : console.log("empty")
