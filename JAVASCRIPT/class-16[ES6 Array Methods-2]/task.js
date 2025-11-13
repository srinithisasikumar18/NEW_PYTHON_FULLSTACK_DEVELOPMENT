let employees = [
    {
        "id": 1,
        "name": "Natty",
        "gender": "Male"
    },
    {
        "id": 2,
        "name": "Mozelle",
        "gender": "Female"
    },
    {
        "id": 3,
        "name": "Roderick",
        "gender": "Male"
    },
    {
        "id": 4,
        "name": "Lucky",
        "gender": "Female"
    },
    {
        "id": 5,
        "name": "Roger",
        "gender": "Male"
    },
    {
        "id": 6,
        "name": "Natale",
        "gender": "Male"
    },
    {
        "id": 7,
        "name": "Brade",
        "gender": "Male"
    },
    {
        "id": 8,
        "name": "Clarita",
        "gender": "Female"
    },
    {
        "id": 9,
        "name": "Rob",
        "gender": "Male"
    },
    {
        "id": 10,
        "name": "Sileas",
        "gender": "Female"
    },
    {
        "id": 11,
        "name": "Gualterio",
        "gender": "Male"
    },
    {
        "id": 12,
        "name": "Lazare",
        "gender": "Male"
    },
    {
        "id": 16,
        "name": "Lazare",
        "gender": "Male"
    },
    {
        "id": 13,
        "name": "Leicester",
        "gender": "Agender"
    },
    {
        "id": 14,
        "name": "Joline",
        "gender": "Female"
    },
    {
        "id": 15,
        "name": "Armand",
        "gender": "Male"
    }
]
let male_emp = employees.filter((emp) => emp.gender === 'Male')
console.log(male_emp)
let employeee = employees.find((emp) => {
    return emp.name === "Lazare"
})
console.log(employeee)