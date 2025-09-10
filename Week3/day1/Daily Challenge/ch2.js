let pattern = ""; // to store the stars
//Using a single loop
for (let i = 1; i <= 6; i++) {
    pattern += "* ";       // add a star and a space
    console.log(pattern);  // print the current pattern
}
//Using nested loops
for (let i = 1; i <= 6; i++) { // outer loop for each line
    let line = "";
    for (let j = 1; j <= i; j++) { // inner loop to add stars
        line += "* ";
    }
    console.log(line); // print the line after inner loop
}
