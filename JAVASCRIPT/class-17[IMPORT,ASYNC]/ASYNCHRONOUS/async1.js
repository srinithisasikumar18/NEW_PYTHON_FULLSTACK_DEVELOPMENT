//promise:: contains two arguements--->>>> resolve and reject

let goa = (Success, failure) => {
    let acc_bal = 10000
    acc_bal >= 30000 ? Success("go to goa") : failure("go to home")

}

goa((msg) => { console.log(msg) }, (err) => { console.log(err) })