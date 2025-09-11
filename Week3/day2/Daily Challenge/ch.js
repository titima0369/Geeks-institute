
const planets = [
  { name: "Mercury", color: "#909090", moons: 0 },
  { name: "Venus",   color: "#E6C27A", moons: 0 },
  { name: "Earth",   color: "#3B82F6", moons: 1 },
  { name: "Mars",    color: "#D94E3C", moons: 2 },
  { name: "Jupiter", color: "#D9A066", moons: 4 }, 
  { name: "Saturn",  color: "#CDA45E", moons: 3 }, 
  { name: "Uranus",  color: "#7FD3E6", moons: 2 },
  { name: "Neptune", color: "#2B5DAA", moons: 1 }
];


const section = document.querySelector(".listPlanets");


if (!section) {
  console.error("No .listPlanets section found in DOM. Make sure index.html includes <section class='listPlanets'></section>");
}


function degToRad(deg) { return deg * Math.PI / 180; }


planets.forEach((p, planetIndex) => {

  const wrapper = document.createElement("div");
  wrapper.className = "planet-wrapper";

  
  const planetEl = document.createElement("div");
  planetEl.className = "planet";
  planetEl.style.background = p.color;

  
  const label = document.createElement("div");
  label.className = "label";
  label.textContent = p.name;
  planetEl.appendChild(label);

  wrapper.appendChild(planetEl);

  const moonCount = p.moons;
  const wrapperWidth = parseFloat(getComputedStyle(wrapper).width) || 220; 
  const centerX = wrapperWidth / 2;
  const centerY = wrapperWidth / 2;
  const baseRadius = Math.min(centerX, centerY) - 40; 

  for (let i = 0; i < moonCount; i++) {
    const moon = document.createElement("div");
    moon.className = "moon";

    
    const angleDeg = (i / moonCount) * 360 + (planetIndex * 10); 
    const angle = degToRad(angleDeg);

    const radius = baseRadius + (i * 12) + (Math.random() * 8);

    
    const moonX = centerX + Math.cos(angle) * radius;
    const moonY = centerY + Math.sin(angle) * radius;

    
    moon.style.left = `${moonX}px`;
    moon.style.top = `${moonY}px`;

    
    const moonSize = 12 + Math.round(Math.random() * 8);
    moon.style.width = `${moonSize}px`;
    moon.style.height = `${moonSize}px`;
    moon.style.borderRadius = `${moonSize / 2}px`;

    wrapper.appendChild(moon);
  }

  section.appendChild(wrapper);
});
