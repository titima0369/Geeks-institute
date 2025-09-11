const form = document.getElementById("libform");
const storySpan = document.getElementById("story");
const shuffleBtn = document.getElementById("shuffle-button");

const storyTemplates = [
  (noun, adj, person, verb, place) =>
    `${person} took a ${adj} ${noun} and decided to ${verb} all the way to ${place}.`,
  (noun, adj, person, verb, place) =>
    `In ${place}, ${person} found a ${adj} ${noun} that could ${verb} like no other.`,
  (noun, adj, person, verb, place) =>
    `${person} loved their ${adj} ${noun}, but one day it started to ${verb} in ${place}!`
];

let latestValues = { noun: "", adjective: "", person: "", verb: "", place: "" };

form.addEventListener("submit", (e) => {
  e.preventDefault();

  const noun = document.getElementById("noun").value.trim();
  const adj = document.getElementById("adjective").value.trim();
  const person = document.getElementById("person").value.trim();
  const verb = document.getElementById("verb").value.trim();
  const place = document.getElementById("place").value.trim();

  if (!noun || !adj || !person || !verb || !place) {
    alert("Please fill in all fields!");
    return;
  }

  latestValues = { noun, adjective: adj, person, verb, place };

  generateStory();
});

shuffleBtn.addEventListener("click", () => {
  if (!latestValues.noun) {
    alert("Please fill in the form first!");
    return;
  }
  generateStory();
});

function generateStory() {
  const { noun, adjective, person, verb, place } = latestValues;
  const randomIndex = Math.floor(Math.random() * storyTemplates.length);
  const story = storyTemplates[randomIndex](noun, adjective, person, verb, place);
  storySpan.textContent = story;
}
