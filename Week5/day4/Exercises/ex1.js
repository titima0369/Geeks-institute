// products
const products = [
  { name: "Laptop", price: 1000, category: "Electronics" },
  { name: "Phone", price: 600, category: "Electronics" },
  { name: "Book", price: 20, category: "Education" },
  { name: "Shoes", price: 50, category: "Fashion" }
];

module.exports = products; // CommonJS export
// shop
const products = require("./products");

function findProduct(productName) {
  return products.find(p => p.name.toLowerCase() === productName.toLowerCase());
}

console.log(findProduct("Laptop"));
console.log(findProduct("Shoes"));
console.log(findProduct("Book"));
