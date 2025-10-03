let guestList  = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina",
};
let name = prompt("Enter your name : ").value;
for (guest of Object.values(guestList)) {
    if (guest == name ) {
    console.log(`Your country is ${guestList[guest]}`);
    console.log(`Hi! I'm ${name}, and I'm from ${guestList[guest]}.`);
    } else {
        console.log("Hi! I'm a guest.")
}
}
// if (guestList.norman == name ) {
//   console.log(`Your country is ${guestList.norman}`);
//   console.log(`Hi! I'm ${name}, and I'm from ${guestList.norman}.`);
// } else {
//     console.log("Hi! I'm a guest.")
// }

