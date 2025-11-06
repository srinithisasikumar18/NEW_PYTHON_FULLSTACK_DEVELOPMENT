//it has to execute for every second
// settimeout()=>{}(a,b)--excepting function and time interval,, setintervale(a,b)---function and time interval
//settimeout--execute provided function after time interval. js inbuilt function
//setInterval--executes continousously for a given interval of time
//fetch---
setInterval(() => {
    console.log("gm");

}, 2000)

setInterval(function () { console.log("gm") }, 1000)