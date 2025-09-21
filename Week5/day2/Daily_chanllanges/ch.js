const form = document.getElementById("gifForm");
const input = document.getElementById("categoryInput");
const gifContainer = document.getElementById("gifContainer");
const deleteAllBtn = document.getElementById("deleteAll");

const API_KEY = "hpvZycW22qCjn5cRM1xtWB8NKq4dQ2My";

form.addEventListener("submit", async (e) => {
  e.preventDefault();
  const category = input.value.trim();

  if (!category) return;

  const url = `https://api.giphy.com/v1/gifs/random?tag=${category}&rating=g&api_key=${API_KEY}`;

  try {
    const response = await fetch(url);
    if (!response.ok) {
      throw new Error("Network error: " + response.status);
    }
    const data = await response.json();
    const gifUrl = data.data.images.original.url;

    const gifCard = document.createElement("div");
    gifCard.classList.add("gif-card");

    const img = document.createElement("img");
    img.src = gifUrl;
    img.alt = category;

    const delBtn = document.createElement("button");
    delBtn.textContent = "DELETE";
    delBtn.classList.add("delete-btn");
    delBtn.addEventListener("click", () => {
      gifCard.remove();
    });

    gifCard.appendChild(img);
    gifCard.appendChild(delBtn);
    gifContainer.appendChild(gifCard);

  } catch (error) {
    console.error("Fetch error:", error);
  }

  input.value = "";
});

deleteAllBtn.addEventListener("click", () => {
  gifContainer.innerHTML = "";
});
