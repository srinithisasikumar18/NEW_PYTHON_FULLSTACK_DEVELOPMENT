let enames = ["rahul", "sonia", "priya", "modi"]
let lenght_name = enames.reduce((n, names) => {
    return n + names.length;
}
    , 0
);
console.log(lenght_name);