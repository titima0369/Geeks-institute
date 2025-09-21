const randomBtn = document.getElementById("randomBtn");
const loading = document.getElementById("loading");
const characterInfo = document.getElementById("characterInfo");
const errorMsg = document.getElementById("errorMsg");

const nameEl = document.getElementById("name");
const heightEl = document.getElementById("height");
const genderEl = document.getElementById("gender");
const birthYearEl = document.getElementById("birth_year");
const homeworldEl = document.getElementById("homeworld");

const BASE_URL = "https://www.swapi.tech/api/people/";

function getRandomId() {
  return Math.floor(Math.random() * 83) + 1;
}

async function fetchCharacter() {

  characterInfo.classList.add("hidden");
  errorMsg.classList.add("hidden");
  loading.classList.remove("hidden");

  const id = getRandomId();

  try {
    const response = await fetch(`${BASE_URL}${id}`);
    if (!response.ok) {
      throw new Error(`Error: ${response.status}`);
    }
    const data = await response.json();
    const char = data.result.properties;

    let homeworldName = "Unknown";
    try {
      const homeResponse = await fetch(char.homeworld);
      if (homeResponse.ok) {
        const homeData = await homeResponse.json();
        homeworldName = homeData.result.properties.name;
      }
    } catch {}

    nameEl.textContent = char.name;
    heightEl.textContent = char.height;
    genderEl.textContent = char.gender;
    birthYearEl.textContent = char.birth_year;
    homeworldEl.textContent = homeworldName;

    loading.classList.add("hidden");
    characterInfo.classList.remove("hidden");
  } catch (error) {
    loading.classList.add("hidden");
    errorMsg.textContent = "❌ Failed to load character data. Try again.";
    errorMsg.classList.remove("hidden");
    console.error(error);
  }
}

randomBtn.addEventListener("click", fetchCharacter);
