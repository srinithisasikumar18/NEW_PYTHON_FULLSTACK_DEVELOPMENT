function calculateGrade() {
    let name = document.getElementById("name").value;
    let sub1 = Number(document.getElementById("sub1").value);
    let sub2 = Number(document.getElementById("sub2").value);
    let sub3 = Number(document.getElementById("sub3").value);
    let avg = (sub1 + sub2 + sub3) / 3
    let grade;
    if (avg >= 90) {
        grade = "A";
    }
    else if (avg >= 75) {
        grade = "B";
    }
    else {
        grade = "Fail";
    }

    document.getElementById('result').innerHTML = grade;
}