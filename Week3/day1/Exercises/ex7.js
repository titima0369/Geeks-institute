const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];


let firstLetters = [];
for (let i = 0; i < names.length; i++) {
  firstLetters.push(names[i][0]);
}


firstLetters.sort();


let secretName = firstLetters.join("");


console.log(secretName);
