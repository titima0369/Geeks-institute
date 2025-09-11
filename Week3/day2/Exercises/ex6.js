const navBar = document.getElementById("navBar");
navBar.setAttribute("id", "socialNetworkNavigation");

const newLi = document.createElement("li");
const logoutText = document.createTextNode("Logout");
newLi.appendChild(logoutText);
navBar.querySelector("ul").appendChild(newLi);

const firstLi = navBar.querySelector("ul").firstElementChild;
const lastLi = navBar.querySelector("ul").lastElementChild;
console.log("First link:", firstLi.textContent);
console.log("Last link:", lastLi.textContent);