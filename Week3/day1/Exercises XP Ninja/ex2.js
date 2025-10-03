function findAvg(gradesList) {
    let sum = 0;
    let avg = 0;
    for (let i = 0; i < gradesList.length; i++) {
        sum += gradesList[i];
    }
    avg = sum / gradesList.length;
    return avg;
}
console.log(`The average is ${findAvg([40, 98, 89, 100, 15, 86, 94])}`);


function failedOrPassed(gradesList) {
    let avg = findAvg(gradesList);
    if (avg < 65 ) {
        console.log("You FAILED and must repeat the course ");
    } else {
        console.log("You PASSED the course successfully, congrats!");
    }
}
failedOrPassed([40, 98, 89, 100, 15, 86, 94]);