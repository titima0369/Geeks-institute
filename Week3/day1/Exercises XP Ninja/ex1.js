let person1 = {
  firstName: "John",
  Mass: 70,
  Height: 1.75,
};
let person2 = {
  firstName: "Jane",
  Mass: 60,
  Height: 1.65,
};
let bmi = function(Mass, Height) {
    return Mass / (Height * Height);
}
let bmi1 = bmi(person1.Mass, person1.Height);
let bmi2 = bmi(person2.Mass, person2.Height);
let theLowestBmi = function(bmi1, bmi2) {
    if (bmi1 > bmi2) {
        console.log(`${person2.firstName} has the lowest BMI`);
    } else {
        console.log(`${person2.firstName} has the lowest BMI`);
    }
}
theLowestBmi(bmi1, bmi2);