
let number = Number(prompt("Please enter a number:"));

while (number < 10) {
  number = Number(prompt("The number is too small. Please enter a new number:"));
}

console.log("Great! The number you entered is " + number);
