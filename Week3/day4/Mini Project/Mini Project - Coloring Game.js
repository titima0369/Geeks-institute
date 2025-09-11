const grid = document.getElementById("grid");
const colorPicker = document.getElementById("colorPicker");
const clearBtn = document.getElementById("clearBtn");
const eraserBtn = document.getElementById("eraserBtn");
const sizeRange = document.getElementById("sizeRange");
const sizeLabel = document.getElementById("sizeLabel");

let isDrawing = false;
let currentColor = colorPicker.value;
let eraserMode = false;

function updateSizeLabel(size) {
  sizeLabel.textContent = `${size} x ${size}`;
}

function createGrid(size) {
  grid.innerHTML = "";
  grid.style.gridTemplateColumns = `repeat(${size}, 20px)`;

  const total = size * size;
  for (let i = 0; i < total; i++) {
    const cell = document.createElement("div");
    cell.className = "square";
    cell.style.background = "white";

    cell.addEventListener("mousedown", (e) => {
      e.preventDefault();
      paintCell(cell);
      isDrawing = true;
    });

    cell.addEventListener("mouseover", () => {
      if (isDrawing) paintCell(cell);
    });

    cell.addEventListener("touchstart", (e) => {
      e.preventDefault();
      paintCell(cell);
    });
    cell.addEventListener("touchmove", (e) => {
      const touch = e.touches[0];
      const el = document.elementFromPoint(touch.clientX, touch.clientY);
      if (el && el.classList.contains("square")) paintCell(el);
    }, { passive: false });

    grid.appendChild(cell);
  }
}

function paintCell(cell) {
  if (eraserMode) {
    cell.style.background = "white";
  } else {
    cell.style.background = currentColor;
  }
}

document.addEventListener("mouseup", () => {
  isDrawing = false;
});

colorPicker.addEventListener("input", (e) => {
  currentColor = e.target.value;
  eraserMode = false;
  eraserBtn.classList.remove("active");
});

clearBtn.addEventListener("click", () => {
  document.querySelectorAll(".square").forEach(s => s.style.background = "white");
});

eraserBtn.addEventListener("click", () => {
  eraserMode = !eraserMode;
  eraserBtn.classList.toggle("active", eraserMode);
});

sizeRange.addEventListener("input", (e) => {
  const size = parseInt(e.target.value, 10);
  updateSizeLabel(size);
  createGrid(size);
});

updateSizeLabel(sizeRange.value);
createGrid(parseInt(sizeRange.value, 10));
