const ordinal = ["th","st","nd","rd"];
colors.forEach((color, index) => {
    let suffix = (index + 1 <= 3) ? ordinal[index + 1] : ordinal[0];
    console.log(`${index + 1}${suffix} choice is ${color}.`);
});