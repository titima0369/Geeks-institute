// Exercise 3
async function getStarship() {
  try {
    const response = await fetch("https://www.swapi.tech/api/starships/9/");
    if (!response.ok) {
      throw new Error("Network response was not ok " + response.status);
    }
    const data = await response.json();
    console.log(data.result);
  } catch (error) {
    console.log("Fetch error: ", error);
  }
}

getStarship();
