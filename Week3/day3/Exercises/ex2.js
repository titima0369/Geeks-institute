const form = document.querySelector("form");
console.log(form);

const fname = document.getElementById("fname");
const lname = document.getElementById("lname");
console.log(fname, lname);

const inputsByName = document.getElementsByName("firstname");
console.log(inputsByName);

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const first = fname.value.trim();
  const last = lname.value.trim();

  if (first && last) {
    const ul = document.querySelector(".usersAnswer");
    ul.innerHTML = ""; 
    [first, last].forEach(val => {
      const li = document.createElement("li");
      li.textContent = val;
      ul.appendChild(li);
    });
  }
});
