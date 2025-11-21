let eids = [101, 102, 103, 104, 105]
let uids = []
for (let eid of eids) {
    uids.push(eid)
}

let uiids = eids((eid) => {
    return eid
})

let uiiids = [...eids]
console.log(uiids)