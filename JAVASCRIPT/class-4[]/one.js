let employee=[
    {"eid":101,"ename":"srinithi","esal":45000.56},
    {"eid":102,"ename":"kokila","esal":56000.56},
    {"eid":103,"ename":"sasi","esal":55000.56},
    {"eid":104,"ename":"karthik","esal":85000.56}
]
//print all employees names:
console.log(employee[0].ename)
console.log(employee[1].ename)
console.log(employee[2].ename)
console.log(employee[3].ename)
//using "FOR OF" we can available to print names,id
for(emp of employee){
    console.log(emp)
    console.log(emp.eid)
    console.log(emp.esal)
    console.log("name of emp is:",emp.ename)
}
