// data
export const people = [
  { name: "Alice", age: 25, location: "New York" },
  { name: "Bob", age: 30, location: "London" },
  { name: "Charlie", age: 35, location: "Paris" }
];
// app
import { people } from "./data.js";

function calculateAverageAge(persons) {
  const total = persons.reduce((sum, p) => sum + p.age, 0);
  return total / persons.length;
}

console.log("Average age:", calculateAverageAge(people));
