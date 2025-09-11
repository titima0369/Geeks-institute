let allBoldItems = [];

function getBoldItems() {
  allBoldItems = document.querySelectorAll("#sentence strong");
}
getBoldItems();

function highlight() {
  allBoldItems.forEach(item => item.style.color = "blue");
}

function returnItemsToDefault() {
  allBoldItems.forEach(item => item.style.color = "black");
}

const paragraph = document.getElementById("sentence");
paragraph.addEventListener("mouseover", highlight);
paragraph.addEventListener("mouseout", returnItemsToDefault);
