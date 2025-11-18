let gotoGoa = (resolve, reject) => {
    let acc_bal = 5000
    if (acc_bal >= 10000) {
        resolve("Enjoy")
    }
    else {
        reject("Practice")
    }
}
gotoGoa((msg) => { console.log(msg) }, (err) => { console.log(err) })