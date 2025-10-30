function changeColor(){
    document.getElementById('first').style.backgroundColor="Yellow"
}
function mouseOut(){
    document.getElementById('second').style.backgroundColor='Orange'
}
function onClick(){
    document.getElementById('three').style.backgroundColor='Green'
}
function ondblCLick(){
    document.getElementById('four').style.backgroundColor='white'
}
function onFocus(){
    document.getElementById('five').style.backgroundColor='Pink'
}
function onBlur(){
    let input=document.getElementById('six');
    input.value=input.value.toUpperCase();
    input.value=input.value.toLowerCase();
}