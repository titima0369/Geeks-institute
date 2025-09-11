const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];
const epicString = epic.reduce((acc, word) => acc + " " + word);
console.log(epicString);