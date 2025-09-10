
const family = {
  father: "John",
  mother: "Mary",
  son: "Alex",
  daughter: "Emma"
};

console.log("Keys of the family object:");
for (let key in family) {
  console.log(key);
}

console.log("Values of the family object:");
for (let key in family) {
  console.log(family[key]);
}
