const formSphere = document.getElementById("MyForm");
formSphere.addEventListener("submit", (e) => {
  e.preventDefault();

  const radius = parseFloat(document.getElementById("radius").value);
  if (isNaN(radius) || radius <= 0) {
    alert("Please enter a valid radius");
    return;
  }

  const volume = (4 / 3) * Math.PI * Math.pow(radius, 3);
  document.getElementById("volume").value = volume.toFixed(2);
});
