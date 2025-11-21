let cars = [
    { "brand": "Maruti Suzuki", "model": "Swift", "price": 650000, "color": "Red" },
    { "brand": "Maruti Suzuki", "model": "Baleno", "price": 800000, "color": "Blue" },
    { "brand": "Hyundai", "model": "i20", "price": 900000, "color": "White" },
    { "brand": "Hyundai", "model": "Venue", "price": 1100000, "color": "Black" },
    { "brand": "Tata", "model": "Nexon", "price": 1200000, "color": "Grey" },
    { "brand": "Tata", "model": "Punch", "price": 700000, "color": "Orange" },
    { "brand": "Mahindra", "model": "XUV300", "price": 1300000, "color": "Silver" },
    { "brand": "Mahindra", "model": "Thar", "price": 1600000, "color": "Black" },
    { "brand": "Honda", "model": "Amaze", "price": 850000, "color": "White" },
    { "brand": "Honda", "model": "City", "price": 1400000, "color": "Red" },
    { "brand": "Toyota", "model": "Glanza", "price": 900000, "color": "Blue" },
    { "brand": "Toyota", "model": "Innova Crysta", "price": 2200000, "color": "Silver" },
    { "brand": "Kia", "model": "Seltos", "price": 1500000, "color": "Black" },
    { "brand": "Kia", "model": "Sonet", "price": 1100000, "color": "Grey" },
    { "brand": "Renault", "model": "Kwid", "price": 550000, "color": "Yellow" },
    { "brand": "Renault", "model": "Triber", "price": 800000, "color": "White" },
    { "brand": "Skoda", "model": "Slavia", "price": 1400000, "color": "Blue" },
    { "brand": "Volkswagen", "model": "Virtus", "price": 1500000, "color": "Red" },
    { "brand": "MG", "model": "Hector", "price": 1800000, "color": "White" },
    { "brand": "Nissan", "model": "Magnite", "price": 900000, "color": "Silver" }
]

// let car = cars.sort((car, price) => { 0 - 1 })
// console.log(car)
// let car = cars.sort((car1, car2) => { car1.price - car2.price })
// console.log(car)

// let car = cars.map((car) => {
//     car.onroadprice = car.price + 50000
//     return car
// })
// console.log(car)

/* let new_car = cars.map(car => car.onroadprice = car.price + 50000)
console.log(new_car) */

// let car_color = cars.map((car) => car.color)
// console.log([...new Set(car_color)])

// let car_colors = new Set(cars.map(car => car.color))
// console.log(car_colors)

// let new_color = [...new Set(cars.color)]
// console.log(new_color)


let [c1, c2, c3] = [cars[0], cars[1], cars[2]]
console.log(c1)
console.log(c2)
console.log(c3)