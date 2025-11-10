emp = { eid: 101, ename: "rahul", email: 'rahu@gmail' }
details = { email: 'rahhul@pm.com', loc: 'wyanad' }
let emp_details = { ...emp, ...details }
console.log(emp_details)