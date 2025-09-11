const container = document.getElementById("container");
console.log(container);


document.querySelectorAll(".list")[0].children[1].textContent = "Richard";

document.querySelectorAll(".list")[1].children[1].remove();


const lists = document.querySelectorAll(".list");
for (let ul of lists) {
  ul.firstElementChild.textContent = "YourName";
}

for (let ul of lists) {
  ul.classList.add("student_list");
}

lists[0].classList.add("university", "attendance");

container.style.backgroundColor = "lightblue";
container.style.padding = "20px";

const liItems = document.querySelectorAll("li");
for (let li of liItems) {
  if (li.textContent === "Dan") {
    li.style.display = "none";
  }
}

for (let li of liItems) {
  if (li.textContent === "Richard") {
    li.style.border = "2px solid black";
  }
}

document.body.style.fontSize = "18px";

if (container.style.backgroundColor === "lightblue") {
  const names = [...document.querySelectorAll(".list:first-of-type li")]
                .map(li => li.textContent);
  alert(`Hello ${names[0]} and ${names[1]}`);
}