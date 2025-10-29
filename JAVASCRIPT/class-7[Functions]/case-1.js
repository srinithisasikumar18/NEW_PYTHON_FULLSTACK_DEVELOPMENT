function cal(){
    let numbers=[10,20,25,30,45]
    for(let nums of numbers){
        if(nums%2!==0){
            return;
        }
        console.log(nums)
    }
    console.log("good morning")
}
cal()


//if break::10 20 good morning
//if return::