function kgToGrams(weight) {
    return weight * 1000;
}
console.log(kgToGrams(5));
const kgToGrams2 = function(weight) {
    return weight * 1000;
};
console.log(kgToGrams2(3)); 
const kgToGrams3 = weight => weight * 1000;
console.log(kgToGrams3(7)); 
