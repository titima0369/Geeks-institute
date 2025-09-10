// Part I - Arrays
const people = ["Greg", "Mary", "Devon", "James"];



people.shift(); // removes the first element

people[people.indexOf("James")] = "Jason";



people.push("YourName");



console.log("Index of Mary:", people.indexOf("Mary")); // 0


const newPeople = people.slice(1, people.length - 1);
console.log("New people array:", newPeople); 


console.log("Index of Foo:", people.indexOf("Foo"));


const last = people[people.length - 1];
console.log("Last element:", last); 

// Part II - Loops


console.log("All people:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
}

console.log("Loop stops after Devon:");
for (let i = 0; i < people.length; i++) {
  console.log(people[i]);
  if (people[i] === "Devon") {
    break;
  }
}
