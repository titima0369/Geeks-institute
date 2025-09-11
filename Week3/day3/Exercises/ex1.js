const h1 = document.querySelector("h1");
console.log(h1.textContent);

const article = document.querySelector("article");
article.removeChild(article.lastElementChild);

const h2 = document.querySelector("h2");
h2.addEventListener("click", () => {
  h2.style.backgroundColor = "red";
});

const h3 = document.querySelector("h3");
h3.addEventListener("click", () => {
  h3.style.display = "none";
});

const btn = document.getElementById("boldBtn");
btn.addEventListener("click", () => {
  document.querySelectorAll("p").forEach(p => p.style.fontWeight = "bold");
});

h1.addEventListener("mouseover", () => {
  h1.style.fontSize = `${Math.floor(Math.random() * 100)}px`;
});

const secondP = document.querySelectorAll("p")[1];
secondP.addEventListener("mouseover", () => {
  secondP.style.transition = "opacity 1s";
  secondP.style.opacity = "0";
});
