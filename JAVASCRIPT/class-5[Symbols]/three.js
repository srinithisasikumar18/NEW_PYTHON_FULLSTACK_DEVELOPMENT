let eid=Symbol('eid')
let user={
    'eid':101,
    [eid]:102
}
console.log(user.eid)  //101
console.log(user.eid)  //101
console.log(user[eid]) //102-- accessed with the help of []
for(propert in user){
    console.log(propert) // it won't participate in the iteration process as well
}