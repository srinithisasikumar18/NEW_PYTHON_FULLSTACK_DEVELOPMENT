function longTask() {
    for (let i = 0; i < 5000000000; i++) {
        return i
    }

}
console.log("Start");
longTask();     // takes 5 seconds
console.log("End");
