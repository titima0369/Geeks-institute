function hotelCost() {
    let nights;
    do {
        nights = prompt("How many nights would you like to stay in the hotel?");
    } while (isNaN(nights) || nights === "");
    return Number(nights) * 140;
}

function planeRideCost() {
    let destination;
    do {
        destination = prompt("Where are you flying to?");
    } while (!isNaN(destination) || destination === "");

    destination = destination.toLowerCase();
    if (destination === "london") return 183;
    if (destination === "paris") return 220;
    return 300;
}

function rentalCarCost() {
    let days;
    do {
        days = prompt("How many days would you like to rent the car?");
    } while (isNaN(days) || days === "");
    days = Number(days);
    let cost = days * 40;
    if (days > 10) {
        cost *= 0.95; 
    }
    return cost;
}

function totalVacationCost() {
    const hotel = hotelCost();
    const plane = planeRideCost();
    const car = rentalCarCost();

    console.log(`The car cost: $${car}, the hotel cost: $${hotel}, the plane tickets cost: $${plane}.`);
    return hotel + plane + car;
}

totalVacationCost();
