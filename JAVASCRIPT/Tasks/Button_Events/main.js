function changeColor() {
    document.getElementById('first').style.backgroundColor = "Yellow"
}
function mouseOut() {
    document.getElementsByTagName('button')[1].style.backgroundColor = 'Orange'
}
function onClick() {
    document.querySelector('.btn1').style.backgroundColor = 'Green';
}
function ondblCLick() {
    document.getElementsByClassName('four')[0].style.backgroundColor = 'white'
}
function onFocus() {
    document.getElementById('five').style.backgroundColor = 'Pink'
}
function onBlur() {
    let input = document.getElementById('six');
    input.value = input.value.toUpperCase();
    // input.value=input.value.toLowerCase();

}