// fileManager
const fs = require("fs");

function readFile(filePath) {
  return fs.readFileSync(filePath, "utf-8");
}

function writeFile(filePath, content) {
  fs.writeFileSync(filePath, content, "utf-8");
}

module.exports = { readFile, writeFile };
// app
const { readFile, writeFile } = require("./fileManager");

const content = readFile("Hello World.txt");
console.log("Read content:", content);

writeFile("Bye World.txt", "Writing to the file");
console.log("Content written to Bye World.txt");
