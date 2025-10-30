// to print objects in the browser
let eid=101;            
let ename="srinithi"
let avail=true
//we can able to print eid,ename,avail,loc in broswer
// but we can't print emp in the browser instead we have to use JSON.Stringify
let loc=["chennai","bengaluru","salem"]
let emp={
    eid:101,
    ename:"srinithi",
}

document.writeln(eid,"<br>")
document.writeln(ename,"<br>")
document.writeln(avail,"<br>")
document.writeln(loc,"<br>")
document.writeln(emp,"<br>")
//101 srinithi true chennai,bengaluru,salem [object Object]
document.writeln("<br>")
document.writeln(JSON.stringify(emp))